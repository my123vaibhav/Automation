import pytest


@pytest.mark.login
def test_m1():
    assert False


@pytest.mark.login
def test_m2_Login():
    assert 5 == 4


@pytest.mark.home
def test_m3_HomeTest():
    assert "nishant" == "nishant"


@pytest.mark.login
def test_m3_LandingPage():
    assert "abc" != "nishant"


@pytest.mark.home
def test_m4_LandingPage():
    assert "abc" != "nishant"

# run this code:
# PS D:\PythonOCT-12\Python_Session> py.test MarkerUse.py -m login ->>>>>> Run only markup related testcase
# PS D:\PythonOCT-12\Python_Session> py.test .\MarkerUse.py -k LandingPage -v  ----------> run only group related only
