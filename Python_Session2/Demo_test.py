import pytest


def test_m1():
    a = 3
    b = 4
    assert a + 1 == b, "test failed"


def test_m2():
    name = "selenium"
    assert name.upper() == "SELENIUM"


def test_m3():
    assert True


def test_m4():
    assert False


def test_m5():
    assert 100 == 100


def test_m6():
    assert "narwade" == "Narwade"


def test_login():
    assert 20 == 20
