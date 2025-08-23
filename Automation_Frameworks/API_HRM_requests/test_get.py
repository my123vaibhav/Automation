import json

import pytest
from get_helper import HelperGET
from constant import *
import requests


def test_resp_code_for_listuser():
    api=get_api_dict['listuser']
    obj=HelperGET()
    assert obj.check_resp_code_success(api)[0],'failed due to status code'

def test_resp_for_total_page_2():
    api=get_api_dict['listuser']
    obj=HelperGET()
    assert obj.check_total_pages(api,2),'failed due to status code'

def test_resp_for_total_page_7():
    api=get_api_dict['listuser']
    obj=HelperGET()
    assert obj.check_total_pages(api,7),'failed due to status code'

def test_resp_for_total_page_10():
    api=get_api_dict['listuser']
    obj=HelperGET()
    assert obj.check_total_pages(api,10),'failed due to status code'

def test_resp_code_for_single():
    api=get_api_dict['single_user']
    obj=HelperGET()
    assert obj.check_resp_code_success(api)[0],'failed due to status code'

def test_resp_code_for_notfounduser():
    api=get_api_dict['usernotfound']
    obj=HelperGET()
    assert obj.check_resp_code_success(api)[0],'failed due to status code'

def test_resp_code_for_notfounduser_404():
    api=get_api_dict['usernotfound']
    obj=HelperGET()
    assert obj.check_resp_code_success(api)[1]==404,'failed due to status code'

def test_check_id_7():
    api=get_api_dict['listuser']
    obj = HelperGET()
    assert 7 in obj.get_specific_id(api),'failed due to id not present'

def test_check_id_9():
    api=get_api_dict['listuser']
    obj = HelperGET()
    assert 9 in obj.get_specific_id(api),'failed due to id not present'

def test_check_id_8():
    api=get_api_dict['listuser']
    obj = HelperGET()
    assert 8 in obj.get_specific_id(api),'failed due to id not present'

def test_check_id_10():
    api=get_api_dict['listuser']
    obj = HelperGET()
    assert 10 in obj.get_specific_id(api),'failed due to id not present'

def test_check_id_11():
    api=get_api_dict['listuser']
    obj = HelperGET()
    assert 11 in obj.get_specific_id(api),'failed due to id not present'

def test_check_id_12():
    api=get_api_dict['listuser']
    obj = HelperGET()
    assert 11 in obj.get_specific_id(api),'failed due to id not present'

def test_check_id_100():
    api=get_api_dict['listuser']
    obj = HelperGET()
    assert 11 in obj.get_specific_id(api),'failed due to id not present'

@pytest.mark.auth
def test_vusername_vpassword():
    obj=HelperGET()
    assert 'Valide' in obj.check_authentication(usr='admin',pwd='admin'),'Failed due to status code'

@pytest.mark.auth
def test_iusername_vpassword():
    obj=HelperGET()
    assert 'Invalide' in obj.check_authentication(usr='admin123',pwd='admin'),'Failed due to status code'

@pytest.mark.auth
def test_vusername_ipassword():
    obj=HelperGET()
    assert 'Invalide' in obj.check_authentication(usr='admin',pwd='admin@123'),'Failed due to status code'

@pytest.mark.auth
def test_iusername_ipassword():
    obj=HelperGET()
    assert 'Invalide' in obj.check_authentication(usr='admin123',pwd='admin@1234'),'Failed due to status code'


@pytest.mark.auth
def test_eusername_epassword():
    obj=HelperGET()
    assert 'Invalide' in obj.check_authentication(usr='',pwd=''),'Failed due to status code'

@pytest.mark.auth
def test_specusername_spcpassword():
    obj=HelperGET()
    assert 'Invalide' in obj.check_authentication(usr='$%!@#$%',pwd='#!@#@'),'Failed due to status code'

@pytest.mark.auth
def test_numcusername_numpassword():
    obj=HelperGET()
    assert 'Invalide' in obj.check_authentication(usr=12345,pwd=12345),'Failed due to status code'


@pytest.mark.auth
def test_pyusername_password():
    obj=HelperGET()
    assert 'Invalide' in obj.check_authentication(usr='print("hi")',pwd='admin'),'Failed due to status code'


@pytest.mark.auth
def test_marusername_password():
    obj=HelperGET()
    assert obj.check_marathi_authentication(usr='मूलभूत',pwd='admin'),'Failed due to status code'

@pytest.mark.auth
def test_maxusername_password():
    obj=HelperGET()
    str1='chr'*100
    assert 'Invalide' in obj.check_authentication(usr=str1,pwd='admin'),'Failed due to status code'


@pytest.mark.auth
def test_maxusername_password():
    obj=HelperGET()
    u='admin '
    assert 'Invalide' in obj.check_authentication(usr=u,pwd='admin'),'Failed due to status code'

def test_delay_api_with_5():
    obj=HelperGET()
    assert 'within' in obj.check_delay_api(taketime=5),'failed due to resp delay'  #delay<time--pass

def test_delay_api_with_2():
    obj=HelperGET()
    assert 'within' in obj.check_delay_api(taketime=2),'failed due to resp delay'  #delay>time---failed

def test_delay_api_with_3():
    obj=HelperGET()
    assert 'within' in obj.check_delay_api(taketime=3),'failed due to resp delay'  #delay==time---->fail

@pytest.mark.parametrize('api,s',[('https://reqres.in/api/users?page=2',200),('https://reqres.in/api/users/2',200),('https://reqres.in/api/users/23',404),('https://reqres.in/api/users?delay=5',200)])
def test_check_status_code(api,s):
    resp=requests.get(api)
    assert resp.status_code==s,'failed due to status code'

def test_check_empty_resp():
    resp=requests.get('https://reqres.in/api/unknown/23')
    d1=json.loads(resp.content)
    assert len(d1)==0,'failed due to content found'

'''
empty dict

empty json

'''