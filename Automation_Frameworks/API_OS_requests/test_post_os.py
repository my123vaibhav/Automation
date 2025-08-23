import pytest
from helper_os import *
from constant import collection_post_call
from log_os import logger

@pytest.mark.skip
def test_create_user_status_code():
    obj=Helper()
    logger.info('helper is creating...')
    assert obj.check_status_of_post_method(collection_post_call['create_user']),'Failed due to status code'

def test_create_user_status_code():
    obj=Helper()
    logger.info('helper is creating...')
    assert obj.check_status_of_post_method(collection_post_call['create_user']),'Failed due to status code'


def test_create_register_success():
    obj=Helper()
    logger.info('helper is creating...')
    assert obj.check_status_for_register(collection_post_call['register'],success=True),'Failed due to status code'

def test_create_unregister_success():
    obj=Helper()
    logger.info('helper is creating...')
    assert obj.check_status_for_register(collection_post_call['register'],success=False),'Failed due to status code'

def test_login():
    obj=Helper()
    logger.info('helper is creating...')
    assert obj.check_login_function(),'failed due to api'
