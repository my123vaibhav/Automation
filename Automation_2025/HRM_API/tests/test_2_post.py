import pytest
from datetime import datetime
from Helper.requestshelper import RequestHelper
from config.constant import *
from Helper.logger import get_logs

log=get_logs(__name__)

@pytest.mark.order(1)
@pytest.mark.postapi
def test_create_user(header_obj):
    api=create_user_api
    obj1=RequestHelper(api)
    d1={
    "name": "morpheus",
    "job": "leader"}
    actual_status_code=obj1.post_information(ex_status=True,ex_resp=None,data=d1,header=header_obj)
    assert actual_status_code == StatusCode.created, "failed due to status code"
    log.info('status is match')
    result = obj1.post_information(ex_status=None, ex_resp=True, data=d1, header=header_obj)
    assert 'createdAt' in result , "failed due to response , no created field"
    log.info('createdAt is present')
    current_time = datetime.now()
    log.info(f'current time is {current_time}')
    str1 = str(current_time)
    l1 = str1.split()
    assert l1[0] in result['createdAt'] ,"failed due to date"
    log.info('current time match')

@pytest.mark.order(2)
@pytest.mark.postapi
def test_create_user_negative(header_obj):
    api=create_user_api
    obj1=RequestHelper(api)
    d1={"name"}
    actual_status_code=obj1.post_information(ex_status=True,ex_resp=None,data=d1,header=header_obj)
    assert actual_status_code == StatusCode.badreq, "failed due to status code"
    log.info('status is match')

@pytest.mark.order(3)
@pytest.mark.postapi
def test_register_user(header_obj):
    api=register_api
    obj1=RequestHelper(api)
    data={
    "email": "eve.holt@reqres.in",
    "password": "pistol"}
    actual_status_code=obj1.post_information(ex_status=True,ex_resp=None,data=data,header=header_obj)
    assert actual_status_code == StatusCode.ok, "failed due to status code"
    log.info('status code match')
    result=obj1.post_information(ex_status=None,ex_resp=True,data=data,header=header_obj)
    assert 'token' in result ,"failed due to token not available"
    log.info('token is available')

@pytest.mark.order(4)
@pytest.mark.postapi
def test_register_user_negative_with_email(header_obj):
    api=register_api
    obj1=RequestHelper(api)
    data={
    "email": "eve.holt@reqres.in",
    }
    actual_status_code=obj1.post_information(ex_status=True,ex_resp=None,data=data,header=header_obj)
    assert actual_status_code == StatusCode.badreq, "failed due to status code"
    log.info('status code match')
    result=obj1.post_information(ex_status=None,ex_resp=True,data=data,header=header_obj)
    assert "Missing password" in result['error'] , "failed due to response"
    log.info('Missing password validated')


@pytest.mark.order(5)
@pytest.mark.postapi
def test_register_user_negative_with_password(header_obj):
    api=register_api
    obj1=RequestHelper(api)
    data={
    "password": "pistol" }
    actual_status_code=obj1.post_information(ex_status=True,ex_resp=None,data=data,header=header_obj)
    assert actual_status_code == StatusCode.badreq, "failed due to status code"
    log.info('status code match')
    result=obj1.post_information(ex_status=None,ex_resp=True,data=data,header=header_obj)
    assert "Missing email" in result['error'] , "failed due to response"
    log.info('Missing email validated')


@pytest.mark.order(6)
@pytest.mark.postapi
def test_login_user(header_obj):
    api=login_api
    obj1=RequestHelper(api)
    data={
    "email": "eve.holt@reqres.in",
    "password": "cityslicka"}
    actual_status_code=obj1.post_information(ex_status=True,ex_resp=None,data=data,header=header_obj)
    assert actual_status_code == StatusCode.ok, "failed due to status code"
    log.info('status code match')
    result=obj1.post_information(ex_status=None,ex_resp=True,data=data,header=header_obj)
    assert 'token' in result ,"failed due to token not available"
    log.info('token is available')


@pytest.mark.order(7)
@pytest.mark.postapi
def test_login_user_negative(header_obj):
    api=login_api
    obj1=RequestHelper(api)
    data={
    "email": "eve.holt@reqres.in"}
    actual_status_code=obj1.post_information(ex_status=True,ex_resp=None,data=data,header=header_obj)
    assert actual_status_code == StatusCode.badreq, "failed due to status code"
    log.info('status code match')
    result=obj1.post_information(ex_status=None,ex_resp=True,data=data,header=header_obj)
    assert "Missing password" in result['error'], "failed due to error"
    log.info('validation done')

@pytest.mark.order(8)
@pytest.mark.postapi
def test_login_user_negative_without_payload(header_obj):
    api=login_api
    obj1=RequestHelper(api)
    data={}
    actual_status_code=obj1.post_information(ex_status=True,ex_resp=None,data=data,header=header_obj)
    assert actual_status_code == StatusCode.badreq, "failed due to status code"
    log.info('status code match')
    result=obj1.post_information(ex_status=None,ex_resp=True,data=data,header=header_obj)
    assert 'error' in result ,"failed due to error in result"
    assert "Missing email or username" in result['error'], "failed due to error"
    log.info('validation done')


'''
pytest

html---->send

'''