export PYTHONPATH = $(shell pwd)

test: 
	python ./tests/attacher_test.py
