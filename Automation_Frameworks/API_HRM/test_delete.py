import json
from constant import *
import pytest
import requests

@pytest.mark.order(2)
def test_resp_code_204():
    resp=requests.delete(delete_api_dict['user_delete'])
    assert resp.status_code==204,'failed due to status'

@pytest.mark.order(1)
def test_resp_code_200():
    resp=requests.delete(delete_api_dict['user_delete'])
    assert resp.status_code==200,'failed due to status'

@pytest.mark.order(3)
def test_resp_code_wrong_api():
    api=delete_api_dict['user_delete']+'wwwwweertyw'
    resp=requests.delete(api)
    assert resp.status_code==200,'failed due to status'