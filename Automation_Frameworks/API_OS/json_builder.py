'''
this module will responsible for creating json data
this data will used for apis(post,put,patch)
'''
import json


def create_user_data(name,job):  #name= "morpheus" job="leader"
    d1={
        "name": f"{name}",
        "job": f"{job}"
    }
    return json.dumps(d1)   #json object

def register_data(success=None):
    if success:
        d1={
            "email": "eve.holt@reqres.in",
            "password": "pistol"
        }
    else:
        d1 = {
            "email": "sydney@fife"
        }
    return json.dumps(d1)

def login_data(success=None,unsucess=None):
    d1={}
    if success:
        d1={
            "email": "eve.holt@reqres.in",
            "password": "cityslicka"
        }
    if unsucess:
        d1 = {
            "email": "peter@klaven"
        }
    return d1

def update_user():
    d1={
    "name": "morpheus",
    "job": "zion resident"
    }
    return json.dumps(d1)
