import pytest


@pytest.fixture(autouse=True)
def set_up():
    print('starting of test case')
    yield
    print('ending of test case')