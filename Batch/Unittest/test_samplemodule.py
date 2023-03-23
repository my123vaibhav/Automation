import pytest

@pytest.fixture()
def simple_exc():
    ch1='10'
    ans1=int(ch1)
    return ans1

def test_mul(simple_exc):
    assert simple_exc*2==20

