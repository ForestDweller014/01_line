PYTHON = python3

.PHONY = help setup test run clean

FILES = input output

.DEFAULT_GOAL = help

help:
	@echo "---------------HELP-----------------"
	@echo "To test the project type make test"
	@echo "To run the project type make run"
	@echo "------------------------------------"

test:
	${PYTHON} -m main
	
run:
	${PYTHON} main.py

clean:
	rm -r *.project