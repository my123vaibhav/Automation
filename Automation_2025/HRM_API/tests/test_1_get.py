import pytest
from Helper.HRMHelper import HRMHelperClass
from config.constant import *
from Helper.requestshelper import RequestHelper
from Helper.logger import get_logs

log=get_logs(__name__)

@pytest.fixture()
def get_object():
    helperobj = HRMHelperClass()
    return helperobj

@pytest.mark.order(1)
@pytest.mark.getapi
def test_check_status(header_obj,get_object):
    log.info('this is starting of tc')
    api=page_2_api.format(2)
    log.info(f'api is {api}')
    assert get_object.get_status_code(api,header_obj),"failed due to status code"
    result = get_object.get_response(api, header_obj), "failed due to status code"
    assert len(result[0]['data']) > 0, "failed due to resp"

@pytest.mark.order(2)
@pytest.mark.getapi
def test_list_of_resp(header_obj,get_object):
    log.info('this is starting of tc')
    api=page_2_api.format(2)
    log.info(f'api is :{api}')
    result=get_object.get_response(api,header_obj),"failed due to status code"
    assert len(result[0]['data'])>0,"failed due to resp"

@pytest.mark.order(3)
@pytest.mark.getapi
def test_check_status_of_user2(header_obj):
    api=users_api.format(2)
    helperobj=HRMHelperClass()
    assert helperobj.get_status_code(api,header_obj),"failed due to status code"

@pytest.mark.order(4)
@pytest.mark.getapi
def test_check_status_of_user3(header_obj):
    api=users_api.format(3)
    helperobj=HRMHelperClass()
    assert helperobj.get_status_code(api,header_obj),"failed due to status code"

@pytest.mark.order(5)
@pytest.mark.getapi
def test_check_status_of_user4(header_obj):
    api=users_api.format(4)
    helperobj=HRMHelperClass()
    assert helperobj.get_status_code(api,header_obj),"failed due to status code"

@pytest.mark.order(6)
@pytest.mark.getapi
def test_list_content_check_id(header_obj):
    api=page_2_api.format(2)
    helperobj=HRMHelperClass()
    result=helperobj.get_response(api,header_obj),"failed due to status code"
    list_of_id = []
    for i in range(len(result[0]['data'])):
        list_of_id.append(result[0]['data'][i]['id'])
    assert 7 in list_of_id,"failed due to id is not present"
    assert 8 in list_of_id, "failed due to id is not present"
    assert 9 in list_of_id, "failed due to id is not present"
    assert 10 in list_of_id, "failed due to id is not present"
    assert 11 in list_of_id, "failed due to id is not present"
    assert 12 in list_of_id, "failed due to id is not present"

@pytest.mark.order(7)
@pytest.mark.getapi
def test_list_content_check_name(header_obj):
    api=page_2_api.format(2)
    helperobj=HRMHelperClass()
    result=helperobj.get_response(api,header_obj),"failed due to status code"
    list_of_name = []
    for i in range(len(result[0]['data'])):
        list_of_name.append(result[0]['data'][i]['first_name'])
    assert 'Michael' in list_of_name,"failed due to id is not present"
    assert  "Byron" in list_of_name, "failed due to id is not present"

@pytest.mark.order(8)
@pytest.mark.getapi
def test_check_unknow_user(header_obj):
    api=unknow_user
    helperobj=HRMHelperClass()
    assert helperobj.get_status_code(api,header_obj),"failed due to status code"

@pytest.mark.order(9)
@pytest.mark.getapi
def test_check_single_user(header_obj):
    api=single_user
    helperobj=HRMHelperClass()
    assert helperobj.get_status_code(api,header_obj),"failed due to status code"

@pytest.mark.order(10)
@pytest.mark.getapi
def test_check_single_user_2_resp_Data(header_obj):
    ex_id=2
    api=single_user.format(ex_id)
    helperobj=HRMHelperClass()
    result=helperobj.get_response(api,header_obj)
    assert result.get('data','').get('id','') == ex_id , "failed due to id"
    ex_id = 3
    api = single_user.format(ex_id)
    helperobj = HRMHelperClass()
    result = helperobj.get_response(api, header_obj)
    assert result.get('data', '').get('id', '') == ex_id, "failed due to id"

@pytest.mark.order(11)
@pytest.mark.getapi
@pytest.mark.parametrize('exp_id',[(2),(3),(4),(5),(6),(7)])
def test_check_single_user_resp_Data_with_mul(exp_id,header_obj):
    api=single_user.format(exp_id)
    helperobj=HRMHelperClass()
    result=helperobj.get_response(api,header_obj)
    assert result.get('data','').get('id','') == exp_id , "failed due to id"

@pytest.mark.order(12)
@pytest.mark.getapi
def test_check_single_user_resp_Data_negative(header_obj):
    ex_id=23
    api=single_user.format(ex_id)
    helperobj=RequestHelper(api)
    result=helperobj.get_information(ex_status=True,ex_resp=None,ex_time=None,header=header_obj)
    assert result == 404 ,"failed due to status code"
    result = helperobj.get_information(ex_status=None, ex_resp=True, ex_time=None, header=header_obj)
    assert len(result) == 0 , 'failed due to resp'

@pytest.mark.order(13)
@pytest.mark.getapi
def test_check_delay_api(header_obj):
    api=delay_api
    obj1=RequestHelper(api)
    result=obj1.get_information(ex_status=None,ex_resp=None,ex_time=True,header=header_obj)
    assert result > 3 ,"failed due to delay"

@pytest.mark.order(14)
@pytest.mark.getapi
def test_check_delay_api_negative(header_obj):
    api=delay_negative
    obj1=RequestHelper(api)
    result=obj1.get_information(ex_status=None,ex_resp=None,ex_time=True,header=header_obj)
    assert result < 3 ,"failed due to delay"

@pytest.mark.order(15)
@pytest.mark.getapi
def test_check_single_user_resp_Data_negative_abc(header_obj):
    api=unknow_user_abc
    helperobj=RequestHelper(api)
    result=helperobj.get_information(ex_status=True,ex_resp=None,ex_time=None,header=header_obj)
    assert result == 404 ,"failed due to status code"
    result = helperobj.get_information(ex_status=None, ex_resp=True, ex_time=None, header=header_obj)
    assert len(result) == 0 , 'failed due to resp'

'''
[pytest]
addopts = -sv --html report.html --maxfail=1
python_files = test_*.py
python_functions = test_*
python_classes = Test*

markers =
    getapi
    postapi
    putapi
    patchapi
    deleteapi


filehandler-----> to store all the files logs in single file

logger.py
'''