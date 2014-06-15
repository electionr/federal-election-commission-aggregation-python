federal-election-commission-aggregation-python
==============================================

python processing of the fec yaml files


Direct Covenrsion
_________________
html_converter.py  

call like :

    python ../federal-election-commission-aggregation-python/html_converter.py some/dir/

Create index like this :
for x in *.html; do echo "<p><a href=\'$x\'>$x</a></p>"; done > index.html

copy the files to :
2014-pages/data/20140606



First Pass
__________
# this parses a yaml file, uses parser.py 

simple_parser.py     -- produces a huge python file (simpledata.py)
produces one huge python file from the yaml files,
it is the base of all the following process.
note the pretty printed output.

Second Pass
___________

parser2.py        -- parses a large python file
simplify_process.py  -- load a yaml file and convert it to python

# test_report.py  ,test_load.py     to remove, simple loader of one file


Third pass
__________
testsimpledata.py   -- read python files and process them
testsimpledata2.py -- simple processor based on -python loader 

compile_all_data.py  -- try and just compile files
report_json.py	     -- report in json format, work in progress
simpleparser.py   --- jsut strips out a simple formated python file just looks for objects on a line and evals them
resplit_simple_data.py  -- driver to use the simple parser


Helper Classes
______________
parser.py	  -- super simple yaml parser that only recognizes the fech
yaml. defines the Parser class, has no main functions.

pyparser.py       -- parses the python output and splits it again, defines a
Parser class.

Test Drivers
____________
parse.py	  -- driver, parses a whole dir. just produces a report. Does not
do anything productive. 

