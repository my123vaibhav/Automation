import pytest
from helper_os import *
import requests
import json



def test_update_status():
    api="https://reqres.in/api/users/2"
    data={
    "name": "morpheus",
    "job": "zion resident"
    }
    payload=json.dumps(data)
    resp=requests.put(api,payload)
    assert resp.status_code == 200 ,"failed due to status code"


def test_update_resp():
    api="https://reqres.in/api/users/2"
    data={
    "name": "morpheus",
    "job": "zion resident"
    }
    payload=json.dumps(data)
    resp=requests.put(api,payload)
    result=json.loads(resp.content)
    if result['updatedAt']:
        return True
    else:
        return False

def test_update_resp_name():
    api="https://reqres.in/api/users/2"
    data={
    "name": "morpheus",
    "job": "zion resident"
    }
    payload=json.dumps(data)
    resp=requests.put(api,payload)
    result=json.loads(resp.content)
    if result['name']=="morpheus":
        return True
    else:
        return False

def test_update_resp_job():
    api="https://reqres.in/api/users/2"
    data={
    "name": "morpheus",
    "job": "zion resident"
    }
    payload=json.dumps(data)
    resp=requests.put(api,payload)
    result=json.loads(resp.content)
    if result['job']=="zion resident":
        return True
    else:
        return False