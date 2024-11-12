import pytest


# cmd ---> python -m pytest -v -s
# Cmd--> collect only 2 item and not display the output, but it is executed pytest
# go to that folder and apply the above(collected items) cmd--->python -m pytest
# -v -->verbose
# -s-->it will print the print statement
# for particular file need to be executed then use<python -m pytest -v -s .\test_installatio
# nRun2.py>

def testMethod1():
    print("This is test method1")


def testMethod2():
    print("This is test method2")
