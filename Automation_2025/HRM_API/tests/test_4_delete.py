import json

import pytest

from Helper.requestshelper import RequestHelper
from config.constant import *
from Helper.logger import *

log=get_logs(__name__)

@pytest.mark.order(2)
@pytest.mark.deletapi
def test_delete_status_Code(header_obj):
    api=delete_user
    obj1=RequestHelper(api)
    result=obj1.delete_information(header_obj)
    assert result[0] == StatusCode.nocontent , "failed due to status code"
    log.info('status code validation done')

@pytest.mark.order(3)
@pytest.mark.deletapi
def test_delete_response(header_obj):
    api=delete_user
    obj1=RequestHelper(api)
    result=obj1.delete_information(header_obj)   #(status,resp)
    try:
        resp=json.loads(result[1]) if result[1] else True    #if resp is empty---->True
        assert resp
        log.info('response validation done')
    except Exception as e:
        pytest.fail('failed due to expection')

@pytest.mark.order(1)
@pytest.mark.deletapi
def test_delete_non_existing_user(header_obj):
    api=delete_non_existing
    obj1=RequestHelper(api)
    result=obj1.delete_information(header_obj)
    assert result[0] == StatusCode.nocontent , "failed due to status code"
    log.info('status code validation done')
    try:
        resp=json.loads(result[1]) if result[1] else True    #if resp is empty---->True
        assert resp
        log.info('response validation done')
    except Exception as e:
        pytest.fail('failed due to expection')