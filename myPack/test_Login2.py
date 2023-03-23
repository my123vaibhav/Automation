import pytest


# How to execute the particular method by using the below command
# PS D:\Python-NOV15\myPack> python -m pytest -v -s .\test_Login2.py::testmethod1

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
collected 1 item                                                                  

test_Login2.py::testmethod1 Opening the url for login
This is test method1-Login
PASSEDClosing the browser after login

"""
