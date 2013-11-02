"""
Splits the first pass huge python file into smalller files for easier processing
"""

import re
import fnmatch
import os
import pprint
from pyparser import Parser
import sys

pp = pprint.PrettyPrinter(indent=4)

#BLOCKSIZE=100000 #5gb
#BLOCKSIZE=50000 80mb
BLOCKSIZE=7000
#BLOCKSIZE=500 

class Report ():
    def __init__(self):
        self.skip=False
        self.count=0
        self.objcount=0
        self.doopen()

    def doopen(self):
        if (self.count > 0):
            self.doclose()
        self.count = self.count +1
        self.file_name = "data_small/simpledata_%d.py" % self.count
        if not os.path.exists(self.file_name):  #skio
            print("open %s" % self.file_name)
            self.fo = open(self.file_name ,"w")
            self.fo.write("def load() :\n\treturn [\n")
            self.skip=False
        else:
            print("skip %s" % self.file_name)
            self.skip=True

    def add(self,obj):
        self.objcount = self.objcount +1 
        if not self.skip:
            formatted=pp.pformat(obj)
            formatted=formatted.replace("\n"," ") # put them on one line
            self.fo.write(formatted + ",\n")        
        if self.objcount > BLOCKSIZE:
            self.objcount=0
            self.doopen()

    def doclose(self):
        if not self.skip:
            print("close %s" % self.file_name)
            self.fo.write("\n]\n")
            self.fo.flush()    
            self.fo.close()    

    def report(self):
        self.doclose()


r = Report()
p=Parser(r)

#simple test
#x = u""" "FILER'S FEC ID NUMBER": 'C90011628', """
#print p.match_keyvalue(x)

filename= sys.argv[1]
print filename
p.parse_file(filename)
r.report()




