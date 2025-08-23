'''this module is responsible to help the test cases
this module is responsible to verify the APIS

'''
import json


import requests
from constant import *
import json_builder
from log_os import logger

class Helper:
    def __init__(self):
        self.start_url="https://reqres.in/"
        logger.info(f'start url : {self.start_url}')


    def delete_api_status_code(self):
        try:
            logger.info('this function is for delete api status code')
            api=DeleteAPI.delete_user
            logger.info(f'api is : {api}')
            resp=requests.delete(self.start_url+api)
            logger.info(f'response is {resp}')
            if resp.status_code==204:
                logger.info('status code is true')
                return True
            else:
                logger.error('status code is not correct')
                return False
        except Exception as e:
            logger.error(f'function stopped due to {e}')

    def get_list_of_users(self,api='',expected_status=None,expected_resp=None):
        try:
            logger.info('this is get_list_of_users function')
            api=self.start_url+api
            logger.info(f'api is {api}')
            resp=requests.get(api)
            if expected_status:
                logger.info('expected_status is True')
                if resp.status_code == Status_code.success:
                    logger.info(f'{Status_code.success}')
                    return True
                else:
                    logger.error('error due to status code')
                    return False
            if expected_resp:
                logger.info(f'{expected_resp}')
                result=json.loads(resp.content)
                logger.debug(f'result is : {result}')
                if result['total_pages'] == 2:
                    logger.info(f'total pages: {result["total_pages"]}')
                    return True
                else:
                    logger.error('error due to expected_resp')
                    return False
        except Exception as e:
            logger.error(f'exception due to {e}')

    def check_id_from_resp(self):
        try:
            logger.info('starting of check_id_from_resp')
            list_of_id=[]
            api=self.start_url+collection_get_call.get('list_users')
            logger.info(f'api : {api}')
            resp=requests.get(api)
            result=json.loads(resp.content)
            logger.info(f'{result}')
            for i in range(len(result['data'])):
                list_of_id.append(result['data'][i]['id'])
                logger.info(f'id is : {list_of_id}')

            logger.info(f'final ids : {list_of_id}')
            return list_of_id
        except Exception as e:
            logger.error(f'function stopped due to {e}')

    def check_less_than_value(self,val):
        try:
            l1=self.check_id_from_resp()
            logger.info(f'final ids : {l1}')
            final_list=[]
            for i in l1:
                if i<val:
                    final_list.append(i)

            logger.info(f'final ids : {final_list}')
            return final_list
        except Exception as e:
            logger.error(f'function stopped due to {e}')

    def check_id_present(self,val):
        try:
            logger.info(f'check_id_present started...')
            api='https://reqres.in/api/users?page=2'
            resp=requests.get(api)
            result=json.loads(resp.content)
            logger.info(f'val is {val}')
            for i in range(len(result['data'])):
                if result['data'][i]['id']==val:
                    logger.info(f"{result['data'][i]['id']}")
                    return True
                else:
                    logger.error(f'function return False due to val is not matched')
                    return False
        except Exception as e:
            logger.error(f'function stopped due to {e}')

    def check_status_of_post_method(self,api):
        try:
            api=self.start_url+api
            logger.info(f"api is : {api}")
            name= "morpheus"
            job="leader"
            payload=json_builder.create_user_data(name,job)
            logger.info(f"paylod is : {payload}")
            resp=requests.post(api,data=payload)
            logger.info(f"resp is : {resp}")
            if resp.status_code == Status_code.created:
                logger.info(f"status code is : {resp.status_code}")
                return True
            else:
                logger.error(f"status code is : {resp.status_code}")
                return False
        except Exception as e:
            logger.error(f'function stopped due to {e}')


    def check_status_for_register(self,api,success):
        try:
            logger.info(f"starting of check_status_for_register")
            api=self.start_url+api
            logger.info(f"api is {api}")
            payload=json_builder.register_data(success)
            logger.info(f"payload is {payload}")
            resp=requests.post(api,payload)
            if resp.status_code == Status_code.created:
                logger.info(f"response status code is {resp.status_code}")
                return True
            else:
                logger.error(f'failed due to {resp.status_code}')
                return False
        except Exception as e:
            logger.error(f'function stopped due to {e}')

    def check_login_function(self):
        try:
            logger.info(f"started the check_login_function")
            api=self.start_url+collection_post_call['login']
            logger.info(f"api is : {api}")
            payload=json_builder.login_data(success=False,unsucess=True)
            logger.info(f"payload is : {payload}")
            resp=requests.post(api,json.dumps(payload))
            if resp.status_code == 400:
                logger.info(f"response status code is {resp.status_code}")
                return True
            else:
                logger.error(f'failed due to {resp.status_code}')
                return False
        except Exception as e:
            logger.error(f'function stopped due to {e}')


