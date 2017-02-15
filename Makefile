export PYTHONPATH = $(shell pwd)

check: 
	python ./tests/attacher_test.py
