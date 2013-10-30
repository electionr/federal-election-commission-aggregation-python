"""
uses the simple line by line eval parser and json report,
for running on low memory machines
"""
import resource
import os.path
from simpleparser import Parser
from report_json import Report
import sys
import gc

last_res = None

r = Report()
p = Parser(r)


def process(count):

    fname = "data/simpledata_" + str(count) + ".py"

    if not os.path.exists( fname):
        print ("missing %s" % fname)
        return
    count = 0
    p.parse_file(fname)
    
    gc.collect()

for x in range(1,2000):
    try :
        process(x)
        r.report()
    except SyntaxError as e :
        print (e)

r.report()

