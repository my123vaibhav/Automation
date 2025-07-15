import pytest


@pytest.fixture()
def header_obj():
    head={"Content-Type":"application/json","x-api-key":"reqres-free-v1"}
    return head

