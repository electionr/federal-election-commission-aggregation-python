"""
runs import on the python chunk files
"""

import resource
import os.path 
from report import Report


def mem():
    print (resource.getrusage(resource.RUSAGE_SELF))

r=Report()


def process(count):

    fname = "data/simpledata_" + str(count) + ".py"
    name = "data.simpledata_" + str(count)  

    if not os.path.exists( fname):
        print ("missing %s" % fname)
        return
    mem()
    print ("going to import %s" % name)
    mod = __import__(name, fromlist=[])
    print (mod)
    count = 0
    for x in mod.load():
        # use the data
        r.add(x)
        count = count + 1
    print (name, count)

    
for x in range(1,100):
    try :
        process(x)
    except SyntaxError as e :
        print (e)

r.report()

