import pytest

from Helper.requestshelper import RequestHelper
from config.constant import *
from Helper.logger import get_logs

log=get_logs(__name__)

@pytest.mark.order(1)
@pytest.mark.updateapi
def test_put_status_code(header_obj):
    api=update_user
    d1={
    "name": "morpheus",
    "job": "zion resident"}
    obj1=RequestHelper(api)
    actual_status_code=obj1.put_information(ex_status=True,ex_resp=None,ex_time=None,data=d1,header=header_obj)
    assert actual_status_code == StatusCode.ok , "failed due to status code"
    log.info('statuscode validation done')

    resp = obj1.put_information(ex_status=None, ex_resp=True, ex_time=None, data=d1, header=header_obj)
    assert "updatedAt" in resp , "failed due to updated not present in resp"
    log.info('updatedAt is validated successfully')

@pytest.mark.order(2)
@pytest.mark.updateapi
def test_patch_status_code(header_obj):
    api=update_user
    d1={
    "job": "zion resident"}
    obj1=RequestHelper(api)
    actual_status_code=obj1.put_information(ex_status=True,ex_resp=None,ex_time=None,data=d1,header=header_obj)
    assert actual_status_code == StatusCode.ok , "failed due to status code"
    log.info('statuscode validation done')

    resp = obj1.put_information(ex_status=None, ex_resp=True, ex_time=None, data=d1, header=header_obj)
    assert "updatedAt" in resp , "failed due to updated not present in resp"
    log.info('updatedAt is validated successfully')

@pytest.mark.order(3)
@pytest.mark.skip
@pytest.mark.updateapi
def test_patch_status_code_negative(header_obj):
    api=update_user
    d1={"name"}     #set----->json---No
    obj1=RequestHelper(api)
    actual_status_code=obj1.patch_information(ex_status=True,ex_resp=None,ex_time=None,data=d1,header=header_obj)
    assert actual_status_code == StatusCode.badreq , "failed due to status code"
    log.info('statuscode validation done')

    resp = obj1.put_information(ex_status=None, ex_resp=True, ex_time=None, data=d1, header=header_obj)
    assert "Something went wrong" in resp['message'] , "failed due to updated not present in resp"
    log.info('Something went wrong is validated successfully')

