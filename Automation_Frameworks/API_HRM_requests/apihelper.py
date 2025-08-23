import requests
import json
import time

def get_status_code_resp(api,expected_status=None,expected_resp=None):
    try:
        resp = requests.get(api)
        if expected_status:
            return resp.status_code
        if expected_resp:
            return json.loads(resp.content)
    except Exception as e:
        print(str(e))


def get_execution_time(api):
    try:
        resp = requests.get(api)
        return resp.elapsed.total_seconds()
    except Exception as e:
        print(str(e))

def create_data(api,payload):
    try:
        resp=requests.post(api,payload)
        return resp
    except Exception as e:
        print(str(e))


def update_data(api,payload,put=None,patch=None):
    try:
        if put:
            resp=requests.put(api,payload)
            return resp
        if patch:
            resp=requests.patch(api,payload)
            return resp
    except Exception as e:
        print(str(e))


def delete_data(api):
    '''
    this is resp to delete data
    this function will the api
    function will return true if status is 204

    :param api:
    :return:
    '''
    try:
        resp=requests.delete(api)
        if resp.status_code==204:
            return True

        return resp
    except Exception as e:
        print(str(e))

def read_json(filename):
    '''
    This function is responsible to take filename
    and return the data from file
    :param filename:
    :return: data
    '''
    try:
        with open(filename,'r') as file:
            data=json.load(file)   #if data is present inside file---->load
        return data
    except Exception as e:
        print(str(e))



def get_curent_date():
    l1=time.ctime()
    l2=l1.split()
    if l2[1]=='Oct':
        l2[1]='10'
    s=l2[-1]+'-'+l2[1]+'-'+l2[2]
    return s

'''
doctstring----> is used for understand the build--code

comments----> coding--which is not consider in execution

control+/ ---comments #--windows
mac---command+/  mac

select content then press --->/ --linux


POST---> url,payload(json)
post status code-----> ?? 201 created
200---get,delete,put,patch----success
202--->?? accepted

''' '''

'''