from constant import *
from apihelper import *
import requests
class HelperGET:
    def __init__(self):
        self.start='https://reqres.in'


    def check_resp_code_success(self,api):
        try:
            api=self.start+api
            resp=get_status_code_resp(api,expected_status=True)
            if resp==Code.success:
                return True,resp
            else:
                return False,resp
        except Exception as e:
            print(str(e))

    def check_total_pages(self,api,page):
        try:
            api=self.start+api
            resp=get_status_code_resp(api,expected_resp=True)
            if resp['total_pages']==page:
                return True
            else:
                return False
        except Exception as e:
            print(str(e))

    def get_specific_id(self,api):
        all_id=[]
        api=self.start+api
        resp = get_status_code_resp(api, expected_resp=True)
        for i in range(len(resp['data'])):
            all_id.append(resp['data'][i]['id'])
        return all_id

    def check_authentication(self,usr,pwd):
        try:
            resp=requests.get(auth_api,auth=(usr,pwd))
            if resp.status_code==Code.success:
                return 'Valide Credential'
            elif resp.status_code==Code.unth:
                return 'Invalide Credential'
        except Exception as e:
            print(str(e))

    def check_marathi_authentication(self,usr,pwd):
        try:
            resp=requests.get(auth_api,auth=(usr,pwd))
            if resp.status_code==Code.success:
                return 'Valide Credential'
            elif resp.status_code==Code.unth:
                return 'Invalide Credential'
        except UnicodeEncodeError as e:
            return True

    def check_delay_api(self,taketime=0):
        try:
            res=requests.get(delay_api,timeout=taketime)
            if res.status_code==Code.success:
                return 'within given time api is executed'
            else:
                return 'not executed in given time'
        except Exception as e:
            return 'not executed in given time'

# o1=HelperGET()
# api='https://reqres.in/api/users?page=2'
# o1.get_specific_id(api)