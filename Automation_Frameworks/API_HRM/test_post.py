import pytest
from post_helper import *
from apihelper import *

def test_resp_code_create_user():
    obj=POSTHELPER()
    api=post_api_dict['createuser']
    assert obj.create_user(api,expected_status=True),'failed due to status code'

def test_check_resp_create_user():
    obj=POSTHELPER()
    api=post_api_dict['createuser']
    current_time=get_curent_date()
    assert current_time in obj.create_user(api,expected_resp=True),'failed due to status code'

def test_check_reguster_success1():
    obj=POSTHELPER()
    api=post_api_dict['register_success']
    em = 'eve.holt@reqres.in'
    pwd = 'pistol'
    assert obj.create_register_success(api,em,pwd),'failed due to status'

def test_check_register_success2():
    obj=POSTHELPER()
    api=post_api_dict['register_success']
    em = 'vb@ggg'
    pwd = 'pistol'
    assert obj.create_register_success(api,em,pwd),'failed due to status'

def test_check_register_success3():
    obj=POSTHELPER()
    api=post_api_dict['register_success']
    em = 'vb@ggg'
    pwd = 12345
    assert obj.create_register_success(api,em,pwd),'failed due to status '


def test_check_status_code_register_unsuccess():
    obj=POSTHELPER()
    assert obj.check_unsuccess(exp_status=True),'failed due to status code'

def test_check_res_register_unsuccess():
    obj=POSTHELPER()
    assert 'Missing' in obj.check_unsuccess(exp_resp=True),'failed due to status code'

def test_check_res_register_unsuccess_pwd():
    obj=POSTHELPER()
    assert 'password' in obj.check_unsuccess(exp_resp=True),'failed due to status code'

def test_check_res_register_unsuccess_full():
    obj=POSTHELPER()
    assert 'Missing password' in obj.check_unsuccess(exp_resp=True),'failed due to status code'