import json

from constant import *
from apihelper import *
from jsonbuilder import *

class POSTHELPER:
    def __init__(self):
        self.start='https://reqres.in'

    def create_user(self,api,expected_status=None,expected_resp=None):
        try:
            api = self.start + api
            payload=read_json('data.json')
            resp=create_data(api,json.dumps(payload))
            if expected_status:
                if resp.status_code==Code.create:
                    return True
                else:
                    return False
            elif expected_resp:
                d1=json.loads(resp.content)
                return d1.get('createdAt','NOT')
        except Exception as e:
            print(e)

    def create_register_success(self,api,em,pwd):
        try:
            api = self.start + api
            payload=create_json_register(em,pwd)
            resp = create_data(api, json.dumps(payload))
            if resp.status_code==201:
                return True
            else:
                return False
        except Exception as e:
            print(e)

    def check_unsuccess(self,exp_status=None,exp_resp=None):
        try:
            api=self.start+'/api/register'
            d1={"email": "sydney@fife"}
            resp=requests.post(api,json.dumps(d1))
            if exp_status:
                if resp.status_code==400:
                    return True
                else:
                    return False
            elif exp_resp:
                d1=json.loads(resp.content)
                return d1['error']
        except Exception as e:
            print(e)