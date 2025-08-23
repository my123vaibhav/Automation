import pytest
from day7 import check_alerts
'''
this test suite will responsible to take parameters

args[0] -type_alert
args[1] - accept
args[2] -dismiss
args[3] -data
args[4]- value

'''

t1=('info',True,False,"successfully",'Click for JS Alert')
t2=('confirmation',True,False,'OK',"Click for JS Confirm")
t3=('input',True,False,'This is pop',"Click for JS Prompt")

def test_info_alert():
    assert check_alerts(t1),'failed due to alert'

def test_confirmation_alert():
    assert check_alerts(t2),'failed due to alert'

def test_input_alert():
    assert check_alerts(t3),'failed due to alert'
