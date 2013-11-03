"""
simple python parser
just extracts the objects on a line and evals them!
keep the format simple
"""
#import re
#import os
#import fnmatch
class Parser():

    def __init__(self, report):
        self.report=report

    def record(self):
        rec = eval(self.line)
        self.report.add(rec[0])
    
    def match_record(self):

        start = self.line[0]
        end = self.line[-2:-1]
        
        if start=='{' and end=='}':
            self.record()
            return True
        else:
            print "BAD" , self.line
            return False


    def parse_file(self,filename):
        print filename
        ins = open( filename, "r" )
        self.src_file=filename
        for line in ins:
            self.line=line.strip("\n")
            if (len(self.line)>0):
                self.match_record()

