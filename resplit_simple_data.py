"""
uses the simple line by line eval parser and json report,
for running on low memory machines
"""
#import resource
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

start = 1
try :
    start = int(sys.argv[1])
except:
    pass

stop = 3000
try :
    stop = int(sys.argv[2])
except:
    pass

for x in range(start,stop):
    try :
        process(x)
        r.report()
    except SyntaxError as e :
        print (e)

r.report()

