"""
Simple driver to read one yaml file and emit one python file
"""
import yaml
import sys
filename = sys.argv[1]
f = open(filename)
d= f.read()
#print (d )
obj= (yaml.load(d))
import pprint

fo = open(filename + ".py","w")
pp = pprint.PrettyPrinter(indent=4)
fo.write(pp.pformat(obj))
