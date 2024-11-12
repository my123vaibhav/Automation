import requests
ok='200'
def get_Api_Status():
    api='https://reqres.in/api/users?page=2'
    resp=requests.get(api)
    return resp.status_code