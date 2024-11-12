'''this module (test suite) is responsible to validate the APIs'''
import pytest
from helper_os import *
from constant import collection_get_call
from log_os import logger

def test_list_of_users_status_code():
    logger.info('test_list_of_users_status_code')
    obj=Helper()
    logger.info('helper is creating...')
    api=collection_get_call.get('list_users')
    logger.info(f'api is {api}')
    assert obj.get_list_of_users(api=api,expected_status=True),'Failed due to status_code'

def test_single_user_status_code():
    obj=Helper()
    api=collection_get_call.get('single_user')
    logger.info(f'api is {api}')
    assert obj.get_list_of_users(api=api,expected_status=True),'Failed due to status_code'

def test_single_user_not_found_status_code():
    obj=Helper()
    api=collection_get_call.get('single_user_not_found')
    logger.info(f'api is {api}')
    assert obj.get_list_of_users(api=api,expected_status=True),'Failed due to status_code'

def test_list_resource_status_code():
    obj=Helper()
    api=collection_get_call.get('list_resource')
    logger.info(f'api is {api}')
    assert obj.get_list_of_users(api=api,expected_status=True),'Failed due to status_code'

def test_single_resource_status_code():
    obj=Helper()
    api=collection_get_call.get('single_resource')
    assert obj.get_list_of_users(api=api,expected_status=True),'Failed due to status_code'

def test_single_resource_not_found_status_code():
    obj=Helper()
    api=collection_get_call.get('single_resource_not_found')
    logger.info(f'api is {api}')
    assert obj.get_list_of_users(api=api,expected_status=True),'Failed due to status_code'

def test_delay_api_status_code():
    obj=Helper()
    api=collection_get_call.get('delay_api')
    logger.info(f'api is {api}')
    assert obj.get_list_of_users(api=api,expected_status=True),'Failed due to status_code'

def test_list_of_user_total():
    obj=Helper()
    api=collection_get_call.get('list_users')
    logger.info(f'api is {api}')
    assert obj.get_list_of_users(api=api,expected_resp=True),'Failed due to status_code'

def test_list_of_resource_total():
    obj=Helper()
    api=collection_get_call.get('list_resource')
    logger.info(f'api is {api}')
    assert obj.get_list_of_users(api=api,expected_resp=True),'Failed due to status_code'


def test_get_list_users_ids():
    l1=[7,8,9,10,11,12]
    obj=Helper()
    assert obj.check_id_from_resp()==l1,'failed due to id not found'

def test_get_list_users_id_avaiable():
    obj=Helper()
    assert 11 in obj.check_id_from_resp(),'failed due to id not found'

def test_get_list_users_id_not_available():
    obj=Helper()
    assert 110 not in obj.check_id_from_resp(),'failed due to id not found'

def test_get_list_users_id_less_value():
    l1 = [7, 8, 9]
    obj=Helper()
    assert obj.check_less_than_value(10) == l1,'failed due to id not found'

def test_get_list_users_id_less_value_memeory():
    l1 = [7, 8, 9]
    obj=Helper()
    assert obj.check_less_than_value(10) is l1,'failed due to id not found'

def test_get_list_users_id_less_compare_element():
    l1 = [7, 8, 9]
    obj=Helper()
    assert obj.check_less_than_value(10)[0] is l1[0],'failed due to id not found'

def test_id_of_resp():
    obj=Helper()
    assert obj.check_id_present(7),'failed due to the id'
