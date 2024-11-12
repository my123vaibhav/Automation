*** Settings ***
Library    helper.py
Library    data.py

*** Variables ***


*** Keywords ***
verify status code in api
    ${status}=    get_Api_Status
    should be equal as integers    200  ${status}
