"""
produces one huge python file from the yaml files,
it is the base of all the following process.
note the pretty printed output.
"""

#import re
#import fnmatch
#import os
import pprint
from parser import Parser
import sys

pp = pprint.PrettyPrinter(indent=4)

class Report ():
    def __init__(self):
        self.fo = open("simpledata.py","w")
        self.fo.write("def load() :\n\treturn [")

    def add(self,obj):
        self.fo.write(pp.pformat(obj) + ",")

    def report(self):
        self.fo.write("]")


r = Report()
p=Parser(r)
p.parse_dir(sys.argv[1])
r.report()




