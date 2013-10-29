import resource
import os.path 
from report import Report
import sys
import gc

last_res = None

def mem():
    global last_res
    current=resource.getrusage(resource.RUSAGE_SELF)
    print (resource.getrusage(resource.RUSAGE_SELF))
    if last_res:
        #resource.struct_rusage(ru_utime=44.232, ru_stime=0.516, ru_maxrss=963272, ru_ixrss=0, ru_idrss=0, ru_isrss=0, ru_minflt=242030, ru_majflt=8, ru_nswap=0, ru_inblock=72168, ru_oublock=0, ru_msgsnd=0, ru_msgrcv=0, ru_nsignals=0, ru_nvcsw=320, ru_nivcsw=361)
        utime_diff  = current.ru_utime - last_res.ru_utime
        stime_diff  = current.ru_stime - last_res.ru_stime
        maxrss_diff = current.ru_maxrss - last_res.ru_maxrss
        print ("utime %s stime %s maxrss %s" % (utime_diff ,stime_diff, maxrss_diff))

    last_res=current

r=Report()


def process(count):

    fname = "data/simpledata_" + str(count) + ".py"

    module_name = "data.simpledata_" + str(count)  
    code = "import " + module_name 
    code_load = module_name + ".load"
    call_code_load = code_load  + "()"

    if not os.path.exists( fname):
        print ("missing %s" % fname)
        return
    mem()
    print ("going to import %s" % code)
    exec code
    print code
    count = 0
    print (call_code_load)
    for x in eval(call_code_load):
        r.add(x)
        count = count + 1
    print (fname, count)

    # now lets clean up memory
    del x
    del sys.modules[module_name]
    del sys.modules["data"]
    gc.collect()

for x in range(1,259):
    try :
        process(x)
        r.report()
    except SyntaxError as e :
        print (e)

r.report()

