federal-election-commission-aggregation-python
==============================================

python processing of the fec yaml files

First Pass
__________
# this parses a yaml file, uses parser.py 
parse.py	  -- driver, parses a whole dir
parser.py	  -- super simple yaml parser that only recognizes the fech yaml
simple_parser.py     -- produces a huge python file

pyparser.py       -- parses the python output and splits it again


Second Pass
___________

parser2.py        -- parses a large python file 
simple.py	  -- report of fields and count
report.py    
simplify_process.py  -- load a yaml file and convert it to python

testsimpledata.py   -- read python files and process them
testsimpledata2.py -- simple processor based on -python loader 

# test_report.py  ,test_load.py     to remove, simple loader of one file


Third pass
__________
compile_all_data.py  -- try and just compile files
report_json.py	     -- report in json format, work in progress
simpleparser.py   --- jsut strips out a simple formated python file just looks for objects on a line and evals them
resplit_simple_data.py  -- driver to use the simple parser
