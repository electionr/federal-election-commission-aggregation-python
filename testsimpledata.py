import resource
import os.path 
from report import Report

# def delete_module(modname, paranoid=None):
#     from sys import modules
#     try:
#         thismod = modules[modname]
#     except KeyError:
#         raise ValueError(modname)
#     these_symbols = dir(thismod)
#     if paranoid:
#         try:
#             paranoid[:]  # sequence support
#         except:
#             raise ValueError('must supply a finite list for paranoid')
#         else:
#             these_symbols = paranoid[:]
#     print "del modules %s" % modname
#     del modules[modname]
#     for mod in modules.values():
#         try:
#             print "mod %s" % mod
#             print "modname %s" % modname
#             delattr(mod, modname)
#         except AttributeError:
#             pass
#         if paranoid:
#             for symbol in these_symbols:
#                 if symbol[:2] == '__':  # ignore special symbols
#                     continue
#                 try:
#                     delattr(mod, symbol)
#                 except AttributeError:
#                     pass

def mem():
    print resource.getrusage(resource.RUSAGE_SELF)

r=Report()

def process(count):
    mem()

    name = "simpledata_" + str(count)
    pyfile=name + ".py"
    if not os.path.exists( pyfile):
        print "missing %s" % pyfile
        return

    mod = __import__(name, fromlist=[])
    count = 0
    for x in mod.load():
        #print x
        r.add(x)
        count = count + 1
    print (name, count)
    #    delete_module(name)
    
for x in xrange(1,100):
    try :
        process(x)
    except SyntaxError,e :
        print e

r.report()

