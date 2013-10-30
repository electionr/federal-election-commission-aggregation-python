"""
Simple python parser, used to split up the python objects into smaller objects

"""

import re
import os
import fnmatch

class Parser():

    STATE_START  =1
    STATE_FIELD  =2

    re_beginfile     = re.compile(r'\s+return \[\{\s+(.+)')
    re_record        = re.compile(r'([^}]+)\},\{([^{]+)')  # split the old and new record
    re_namevalue1     = re.compile(r'\s*"([^"]+)":\s*"([^"]+)",?')
    re_namevalue2    = re.compile(r'\s*\'([^\']+)\':\s*\'([^\']+)\',?')
    re_namevalue3    = re.compile(r'\s*\'([^\']+)\':\s"([^"]+)",?')
    re_namevalue4    = re.compile(r'\s*\'([^\']+)\':\s*"\'([^\']+)\'",?')
    re_namevalue5    = re.compile(r'\s*\"([^\"]+)\":\s*\'([^\']+)\',?')
    re_namevalue6    = re.compile(r'\s*\'([^\']+)\':\s*"([^"]+)",?')

    def __init__(self, report):
        self.state = Parser.STATE_START
        self.line = ''
        self.record={}
        self.report=report
        self.linecount=0

    def get_line(self):
        return self.line

    def new_record (self):
        if (len(self.record.keys())>0):
            self.report.add(self.record)
        self.record={}
       
    def set_fieldvalue(self,fieldname,value):
        self.record[fieldname]=value

    def match_begin_file(self):
        match = self.re_beginfile.match(self.line)
        if match is not None :
            value = match.group(1)
            self.match_keyvalue(value) # 
            self.state=Parser.STATE_FIELD
            return True
        else:
            return False

    def match_record(self):
        match = self.re_record.match(self.line)
        if match is not None :
            left = match.group(1)
            right = match.group(2)
            self.match_keyvalue(left) # 
            self.new_record()
            self.match_keyvalue(right) # 
            self.state= Parser.STATE_FIELD
            return True
        else:
            return False

    def match_keyvalue(self, line):

        match1 = self.re_namevalue1.match(line)
        match2 = self.re_namevalue2.match(line)
        match3 = self.re_namevalue3.match(line)
        match4 = self.re_namevalue4.match(line)
        match5 = self.re_namevalue5.match(line)
        match6 = self.re_namevalue6.match(line)

        for match in (match1,match2,match3,match4,match5,match6):
            if match is not None :
                name = match.group(1)
                value = match.group(2)
                value = value.strip("\'")
                value = value.rstrip("\'")
                #print name, value
                if value.find("\'")==0:
                    raise Exception(value)
                self.set_fieldvalue(name,value)
                return True

        raise Exception(line)
        return False


    def parse_line(self):
        if self.state == Parser.STATE_START :
            self.match_begin_file()
            if self.linecount > 10:
                raise Exception()
        elif self.state == Parser.STATE_FIELD:
            if  self.match_record():
                #print "REC'%s':'%s'" % ( self.state, self.line)
                pass
            elif (self.match_keyvalue(self.line)):
                pass
            else:
                print "FIELD'%s':'%s'" % ( self.state, self.line)
                pass 
        self.linecount = self.linecount + 1

    def parse_file(self,filename):
        print filename
        ins = open( filename, "r" )
        self.src_file=filename
        for line in ins:
            self.line=line.strip("\n")
#            print self.line
            self.parse_line()
        self.new_record()
