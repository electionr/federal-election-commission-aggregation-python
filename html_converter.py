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
from jinja2 import Environment, PackageLoader

class Report ():
    def __init__(self):
        self.env = Environment(loader=PackageLoader('fechtml', 'templates'))
        template = self.env.get_template('fec_begin_file.html')

    def begin_file(self,filename):
        self.fo = open("output/%s.html" % filename,"w")
        template = self.env.get_template('fec_begin_file.html')
        string = template.render(filename=filename)
        self.fo.write(string)

    def end_file(self,filename):
        template = self.env.get_template('fec_end_file.html')
        self.fo.write(template.render(filename=filename))

    def add(self,obj):
        template = self.env.get_template('fec_record.html')
        obj2={}
        order={}
        for x in obj :
            if isinstance(obj[x], dict):
                v = obj[x]['v']
                v = v.strip('\'')
                v = v.rstrip('\'')
                if v:
                    n= int(obj[x]['n']) +1
                    obj2[x]={ 'v': v,
                              'n' : n
                          }
                    order[n]=x
            else:
                if x == '_record_type':
                    n = 0
                elif x == '_src_file':
                    n = 1

                obj2[x]={ 'v': obj[x],
                          'n' : n } 
                order[n]=x

        self.fo.write(template.render(order=order, obj=obj2 ))

    def report(self):
        self.fo.write("]")


r = Report()
p=Parser(r)
p.parse_dir(sys.argv[1])
r.report()




