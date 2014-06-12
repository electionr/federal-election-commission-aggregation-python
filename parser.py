"""
Simple alternative YAML parser module,
it reads the yaml produced by the new fech module and simplfies it, removing the column number
it does not process failed attempts at coverting, they will need to be repaired first.
Resulting object will be a simple python object for later processing
"""
import re
import os
import fnmatch
class Parser():

    STATE_START  =1
    STATE_FILE  =2
    STATE_RECORD=3
    STATE_FIELD =4
    re_filename = re.compile(r'filename: (.+)')
    re_record   = re.compile(r'  record: (.+)')
    re_name     = re.compile(r'  -\sname: (.+)')
    re_value    = re.compile(r'    value: \'(.+)\'')

    def __init__(self, report):

        self.state = Parser.STATE_START
        self.line = ''
        self.record={}
        self.report=report

    def get_line(self):
        return self.line

    def set_filename(self, filename ):
        self.filename = filename

    def new_record (self):
        if (len(self.record.keys())>0):
            #print str(self.record)

            # remove the empty fields
            rm =[]
            for x in self.record:
                if x in self.record:
                    if self.record[x] == "''":
                        rm.append(x)
                    elif self.record[x] == "":
                        rm.append(x)
            for x in rm :
                del self.record[x]

            self.report.add(self.record)
        self.record={
            '_src_file' : self.src_file
        }

    def set_fieldname(self, field):
        self.fieldname=field
#        print "fieldname '%s'" % ( field)
        
    def set_fieldvalue(self,value):
        self.record[self.fieldname]=value
        #print "'%s':'%s'" % ( self.fieldname, value)
        
    def start(self, pattern):

        match = pattern.match(self.line)
        if match is not None :
            #print "Matched pattern:%s line:%s match:%s" % (pattern, self.line, match)
            return True
        else:
            return False

    def match_value(self):
        match = self.re_value.match(self.line)
        if match is not None :
            value = match.group(1)
            self.set_fieldvalue(value)
            return True
        else:
            return False



    def match_fieldname(self):
        match = self.re_name.match(self.line)
        if match is not None :
            value = match.group(1)
            self.set_fieldname(value)
            self.state= Parser.STATE_FIELD
            return True
        else:
            return False

    def match_file_name(self):
        match = self.re_filename.match(self.line)
        if match is not None :
            value = match.group(1)
            self.set_filename(value)
            self.state=Parser.STATE_FILE
            return True
        else:
            return False

    def set_record_type(self, value) :
        self.record["_record_type"] = value

    def set_file_name(self, value) :
        self.record["_file_name"] = value

    def match_recordtype(self):
        match = self.re_record.match(self.line)
        if match is not None :
            value = match.group(1)
            self.new_record()
            self.set_record_type(value)
            self.state=Parser.STATE_RECORD
            return True
        else:
            return False


    def parse_line(self):
        if self.state == Parser.STATE_START :
            self.match_file_name()

        elif self.state == Parser.STATE_FILE:
            self.match_recordtype()
        elif self.state == Parser.STATE_RECORD:
            self.match_fieldname()
        elif self.state == Parser.STATE_FIELD:
            if (self.match_value()):
                pass
            elif (self.match_fieldname()):
                pass
            elif (self.match_recordtype()):
                pass
            else:
                #print "WHAT2'%s':'%s'" % ( self.state, self.line)
                pass
        else:
            print "WHAT'%s':'%s'" % ( self.state, self.line)
                

    def parse_file(self,filename):
        print filename
        ins = open( filename, "r" )
        self.src_file=filename
        self.report.begin_file(filename)
        for line in ins:
            self.line=line.strip("\n")
            #print "BEFORE:'%s':'%s'" % ( self.state, self.line)
            self.parse_line()
        self.report.end_file(filename)
        self.new_record()
  
    def parse_dir(self,dirname):
        for root, dirnames, filenames in os.walk(dirname):
            for filename in fnmatch.filter(filenames, '*.yml'):
                self.parse_file(os.path.join(root, filename))
