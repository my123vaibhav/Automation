import pytest
import requests
import json
from apihelper import *


def test_resp_code():
    d1={
    "name": "morpheus",
    "job": "zion resident"
    }
    api='https://reqres.in/api/users/2'
    resp=requests.put(api,json.dumps(d1))
    assert resp.status_code==200

def test_resp_updated():
    d1={
    "name": "morpheus",
    "job": "zion resident"
    }
    api='https://reqres.in/api/users/2'
    resp=requests.put(api,json.dumps(d1))
    resp=json.loads(resp.content)
    current_time = get_curent_date()
    assert current_time in resp['updatedAt'],'failed due to update date'





