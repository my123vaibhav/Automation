*** Settings ***
Resource    samplekeyword.robot


*** Test Cases ***
Verify test cases
    [Tags]  p1
    [Documentation]    verify status code
    verify status code in api
