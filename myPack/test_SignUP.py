import pytest


# Selenium with Python Tutorial 41-PyTest | Run Multiple Tests in PyTest
# PS D:\Python-NOV15\myPack> python -m pytest -v -s .\test_SignUP.py
@pytest.fixture()
def setUp():
    print("Opening the url for signUp")
    yield
    print("Closing the browser after signUp")


def testmethod1(setUp):
    print("This is test method1-SignUp")


def testmethod2(setUp):
    print("This is test method2-signUp")


"""
collected 2 items                                                                 

test_SignUP.py::testmethod1 Opening the url for signUp
This is test method1-SignUp
PASSEDClosing the browser after signUp

test_SignUP.py::testmethod2 Opening the url for signUp
This is test method2-signUp
PASSEDClosing the browser after signUp
"""

"""
collected 2 items                                                                 

test_Login.py::testmethod1 Opening the url for login
This is test method1-Login
PASSEDClosing the browser after login

test_Login.py::testmethod2 Opening the url for login
This is test method2-Login
PASSEDClosing the browser after login

# Cmd--> how to executed the folder
#PS D:\Python-NOV15\myPack> python -m pytest -v -s
#
collected 4 items                                                                 

test_Login.py::testmethod1 Opening the url for login
This is test method1-Login
PASSEDClosing the browser after login

test_Login.py::testmethod2 Opening the url for login
This is test method2-Login
PASSEDClosing the browser after login

test_SignUP.py::testmethod1 Opening the url for signUp
This is test method1-SignUp
PASSEDClosing the browser after signUp

test_SignUP.py::testmethod2 Opening the url for signUp
This is test method2-signUp
PASSEDClosing the browser after signUp

CMD--->PS D:\Python-NOV15\myPack> python -m pytest -v -s D:\Python-NOV15\myPack


collected 4 items                                                                 

test_Login.py::testmethod1 Opening the url for login
This is test method1-Login
PASSEDClosing the browser after login

test_Login.py::testmethod2 Opening the url for login
This is test method2-Login
PASSEDClosing the browser after login

test_SignUP.py::testmethod1 Opening the url for signUp
This is test method1-SignUp
PASSEDClosing the browser after signUp

test_SignUP.py::testmethod2 Opening the url for signUp
This is test method2-signUp
PASSEDClosing the browser after signUp




"""
