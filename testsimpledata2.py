import resource
import os.path 
from report import Report
def mem():
    print (resource.getrusage(resource.RUSAGE_SELF))

r=Report()


def process(count):

    fname = "data/simpledata_" + str(count) + ".py"
    code = "import data.simpledata_" + str(count)  
    code2 = "data.simpledata_" + str(count)  + ".load()"

    if not os.path.exists( fname):
        print ("missing %s" % fname)
        return
    mem()
    print ("going to import %s" % code)
    exec code
    print code
    count = 0
    print (code2)
    for x in eval(code2):
        r.add(x)
        count = count + 1
    print (fname, count)

    
for x in range(1,100):
    try :
        process(x)
    except SyntaxError as e :
        print (e)

r.report()

