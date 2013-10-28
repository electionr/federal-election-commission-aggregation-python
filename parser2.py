import re
import fnmatch
import os
import pprint
from pyparser import Parser
import sys

pp = pprint.PrettyPrinter(indent=4)

#BLOCKSIZE=100000 #5gb
BLOCKSIZE=50000 

class Report ():
    def __init__(self):
        self.count=0
        self.objcount=0
        self.doopen()

    def add(self,obj):
        self.objcount = self.objcount +1 
#        print obj
        self.fo.write(pp.pformat(obj) + ",")        
        if self.objcount > BLOCKSIZE:
            self.objcount=0
            self.doopen()

    def doclose(self):
        self.fo.write("]")
        self.fo.close()    

    def doopen(self):
        if (self.count > 0):
            self.doclose()
        self.count = self.count +1
        file_name = "simpledata_%d.py" % self.count
        print(file_name)
        self.fo = open(file_name ,"w")
        self.fo.write("def load() :\n\treturn [")

    def report(self):
        self.close()


r = Report()
p=Parser(r)
filename= sys.argv[1]
print filename
p.parse_file(filename)
r.report()




