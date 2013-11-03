lint :
	~/.local/bin/pylint -E --output-format=parseable *.py

flake :
	~/.local/bin/pyflakes  *.py

test :
	python resplit_simple_data.py

