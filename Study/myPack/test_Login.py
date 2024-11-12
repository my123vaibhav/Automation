import pytest


# Theory-->
# Run all tests in module/file
# python -m pyest -v -s test_Login.py
# python -m pytest -v -s test_SignUp.py

# Run all tests(from all modules ) in a path
# python -m pytest -v -s C:\user\pychar\etc

# Run specific test method from a module
# python -m pytest -v -s test_Login.py::testmethod1


# PS D:\Python-NOV15\myPack> python -m pytest -v -s .\test_Login.py

@pytest.fixture()
def setUp():
    print("Opening the url for login")
    yield
    print("Closing the browser after login")


def testmethod1(setUp):
    print("This is test method1-Login")


def testmethod2(setUp):
    print("This is test method2-Login")


"""
collected 2 items                                                                 

test_Login.py::testmethod1 Opening the url for login
This is test method1-Login
PASSEDClosing the browser after login

test_Login.py::testmethod2 Opening the url for login
This is test method2-Login
PASSEDClosing the browser after login
"""
