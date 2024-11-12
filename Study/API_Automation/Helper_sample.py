import requests
from comman_helper import *
import requests
class helper_sample:
    def __init__(self):
        self.comom_obj=comman_helper()
        self.payload={
    "name": "morpheus",
    "job": "leader"
    }
    def get_api(self,url):
        resp=requests.get(url)
        result=self.comom_obj.validate_api(resp)
        if result:
            return resp
        else:
            return result

    def get_resp(self,url):
        logresult=''
        component='Mycom'
        resp=self.get_api(url)
        try:
            if resp and resp.content:
                logresult=logresult+' '+str(resp.status_code)+component+' '+resp.url+' '+str(resp.elapsed.total_seconds())
        except Exception as e:
                logresult=logresult+str(e)
        finally:
            print(logresult)

    def post_api(self,url):
        resp=requests.post(url,data=self.payload)
        result = self.comom_obj.validate_api_post(resp)
        if result:
            return resp
        else:
            return result

    def post_resp(self,url):
        logresult=''
        component='Mycom'
        resp=self.post_api(url)
        try:
            if resp:
                logresult=logresult+' '+str(resp.status_code)+component+' '+resp.url+' '+str(resp.elapsed.total_seconds())
        except Exception as e:
                logresult=logresult+str(e)
        finally:
            print(logresult)


if __name__=='__main__':
    obj=helper_sample()
    print('-1-')
    obj.get_resp('https://reqres.in/api/users?page=2')
    print('-2-')
    obj.get_resp('https://reqres.in/api/users/2')
    print('-3-')
    obj.get_resp('https://reqres.in/api/users/23')
    print('-4-')
    obj.get_resp('https://reqres.in/api/unknown')
    print('-5-')
    obj.get_resp('https://reqres.in/api/unknown/2')
    print('-6-')
    obj.get_resp('https://reqres.in/api/unknown/23')
    print('-7-')
    obj.get_resp('https://reqres.in/api/users?delay=3')

    print('All post calls')
    print('--8--')
    obj.post_resp('https://reqres.in/api/users')
    print('--9--')
    obj.post_resp('https://reqres.in/api/register')
    print('--10--')
    obj.post_resp('https://reqres.in/api/register')