import json
from requests import get,post,put,patch,delete
from Helper.logger import get_logs
from Helper.jsonbuilder import create_json_data

log=get_logs(__name__)

class RequestHelper:
    def __init__(self,api):
        self.api=api
        log.info(f'api is : {self.api}')

    def get_information(self,ex_status=None,ex_resp=None,ex_time=None,header=None):
        try:
            resp=get(self.api,headers=header)
            log.info(f'resp is : {resp}')
            if ex_status:
                log.info(f'status code is : {resp.status_code}')
                return resp.status_code
            elif ex_resp:
                log.info(f'resp is : {json.loads(resp.content)}')
                return json.loads(resp.content)
            elif ex_time:
                log.info(f'time taken  is : {resp.elapsed.total_seconds()}')
                return resp.elapsed.total_seconds()
        except Exception as e:
            log.error(f'error : {e}')
            return False

    def post_information(self,ex_status=None,ex_resp=None,data=None,header=None):
        try:
            payload=create_json_data(data=data)
            log.info(f'payload is {payload}')
            resp=post(self.api,payload,headers=header)
            log.info(f'response of api : {resp}')
            if ex_status:
                log.info(f'response of api : {resp.status_code}')
                return resp.status_code
            elif ex_resp:
                log.info(f'response of api : {resp.content}')
                return json.loads(resp.content)
        except Exception as e:
            log.error(f'error : {e}')
            return False



    def put_information(self,ex_status=None,ex_resp=None,ex_time=None,data=None,header=None):
        payload=create_json_data(data)
        log.info(f'payload is :{payload}')
        resp=put(url=self.api,data=payload,headers=header)
        log.info(f'response is : {resp}')
        if ex_status:
            return resp.status_code
        elif ex_resp:
            return json.loads(resp.content)
        elif ex_time:
            return resp.elapsed.total_seconds()

    def patch_information(self,ex_status=None,ex_resp=None,ex_time=None,data=None,header=None):
        payload = create_json_data(data)
        log.info(f'payload is :{payload}')
        resp = patch(url=self.api, data=payload, headers=header)
        log.info(f'response is : {resp}')
        if ex_status:
            return resp.status_code
        elif ex_resp:
            return json.loads(resp.content)
        elif ex_time:
            return resp.elapsed.total_seconds()

    def delete_information(self,header):
        resp=delete(self.api,headers=header)
        log.info(f'response is : {resp}')
        return resp.status_code,resp.content

#obj=RequestHelper('url')
#obj.get_information(ex_status=True,header={})
'''
post-----> to create the data /  resourc

dict------> convert----->json

payload----json
post(api,payload)

statuscode-----> 201
response ------> response field----json----> dict---loads
time



'''