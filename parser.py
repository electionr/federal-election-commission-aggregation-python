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

    re_filename = re.compile(r'filename: (.+)')

    STATE_RECORD=3
    re_record   = re.compile(r'  record: (.+)')
    re_name     = re.compile(r'  -\sname: (.+)')
    STATE_IN_NAME =7

    STATE_FIELD =4
    re_value    = re.compile(r'\s+value: (.+)')

    STATE_IN_VALUE =6

    re_number   = re.compile(r'\s+number: \'?(\d+)\'*')

    STATE_INPUT =5
    re_input     = re.compile(r'\- input: (.+)')
    re_count     = re.compile(r'\- (\d)+') # count of rows

    re_input_line= re.compile(r'    .+')

    re_sourceurl = re.compile(r'sourceurl: \!\!python\/unicode \d+')
    re_type      = re.compile(r'type: chunk')
    re_countrow  = re.compile(r'countrows: \d+')
    re_header    = re.compile(r'header: .+')
    re_rows    = re.compile(r'rows:')

    
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
        if self.fieldname not in self.record:
            self.record[self.fieldname]={}
        self.record[self.fieldname]['v']=value
        #print "'%s':'%s'" % ( self.fieldname, value)

    def append_fieldvalue(self,value):
        if self.fieldname not in self.record:
            raise Exception("cannot append to a null field (%s,%s)" % (self.fieldname, value))
        v = self.record[self.fieldname]['v']
        self.record[self.fieldname]['v']=v + value

    def append_field_name(self,value):
        print "appending field name", self.fieldname ,':', value
        self.fieldname=self.fieldname + value


    def set_fieldnumber(self,value):
        if self.fieldname not in self.record:
            self.record[self.fieldname]={}
        self.record[self.fieldname]['n']=value
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
            self.state= Parser.STATE_IN_VALUE
            return True
        else:
            return False

    def match_number(self):
        match = self.re_number.match(self.line)
        if match is not None :
            value = match.group(1)
            self.set_fieldnumber(value)
            return True
        else:
            return False           


    def match_fieldname(self):
        match = self.re_name.match(self.line)
        if match is not None :
            value = match.group(1)
            self.set_fieldname(value)
            self.state= Parser.STATE_IN_NAME
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

    def match_input(self):
        match = self.re_input.match(self.line)
        if match is not None :
            self.state=Parser.STATE_INPUT
            return True
        else:
            return False

    def match_input_content(self):
        match = self.re_input_line.match(self.line)
        if match is not None :
            #print "CONTINUE",self.line
            self.state=Parser.STATE_INPUT
            return True
        else:
            #print "check:",self.line
            return False

    def match_more_value(self):
        '''
        for multi line values
        '''
        match = self.re_input_line.match(self.line)
        if match is not None :
            #print match.group()
            value = match.group()
            self.append_fieldvalue(value)
            return True
        else:
            return False

    def match_more_names(self):
        '''
        for multi line names
        '''
        match = self.re_input_line.match(self.line)
        if match is not None :
            value = match.group()
            self.append_field_name(value)
            return True
        else:
            return False

    def match_x(self,x):
        match = x.match(self.line)
        if match is not None :
            return True
        else:
            #print "check:",self.line
            return False         

    def match_source_url(self):
        return self.match_x(self.re_sourceurl)

    def match_type(self):
        return self.match_x(self.re_type)
       

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
            elif (self.match_number()):
                pass
            elif (self.match_fieldname()):
                pass
            elif (self.match_recordtype()):
                pass
            elif (self.match_input()):
                pass
            elif (self.match_source_url()):
                pass
            elif (self.match_type()):
                pass
            elif (self.match_x(self.re_countrow)):
                pass
            elif (self.match_x(self.re_filename)):
                pass
            elif (self.match_x(self.re_header)):
                pass
            elif (self.match_x(self.re_rows)):
                pass
            elif (self.match_x(self.re_count)):
                pass                

            else:                
                raise Exception("unmatched'%s':'%s'" % ( self.state, self.line))
                pass
        elif self.state == Parser.STATE_INPUT:
            if (self.match_input_content()):
                pass
            elif (self.match_recordtype()):
                pass  # after input
            else:
                raise Exception( "unmatched'%s':'%s'" % ( self.state, self.line)                )

        elif self.state == Parser.STATE_IN_NAME:

            # stop with number
            if (self.match_number()):
                self.state= Parser.STATE_FIELD
            

        elif self.state == Parser.STATE_IN_VALUE:
            if self.match_fieldname()        :
                pass
            if self.match_input():
                pass
            else:
                self.match_more_value()


        else:
            print "WHAT'%s':'%s'" % ( self.state, self.line)
                

    def parse_file(self,filename):
        print filename
        ins = open( filename, "r" )
        self.src_file=filename
        self.report.begin_file(filename)
        number = 0 
        for line in ins:
            number = number + 1
            self.line=line.strip("\n")
            #print "BEFORE:'#%d' '%s':'%s'" % ( number, self.state, self.line)
            self.parse_line()
        self.report.end_file(filename)
        self.new_record()
  
    def parse_dir(self,dirname):
        for root, dirnames, filenames in os.walk(dirname):
            for filename in fnmatch.filter(filenames, '*.yml'):
                self.parse_file(os.path.join(root, filename))
