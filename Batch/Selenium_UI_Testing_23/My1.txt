selenium 3.x
selenium 4.x
Selenium----> framwork----> class, method, variable
            ----> collection modules
            ---> 3rd----> install ---->
                        pip install selenium
             open source---->
             AUT----> python+selenium
webdriver---->??
key:value----> dict----> api---> json
key:value
se-----> dict to json ----> json.dumps()
        python object is coverted to json/XML--->
dese ----> json to dict ----> json.loads()

webdriver----> browser ??
    class inside selenium framework
    from selenium import webdriver -----> module--->
    class---->
            enchapsulation----> binding of data in single unittest
    method----->??? self
    variables-----> ???self-----> web elements----> locators
    locators----> ????

    why ?
    disadvance----->
                    barcode----> manual
                    payment----> manual
                    captcha-----> manual
                    *** ReactJS web pages-----> mo selenium
                    Desktop application---->no selenium
                    No reporting capacity----> report
                                    unittest or pytest

        requirements.txt *****------>100+
                all install packages for framework
                pip install requirements.txt
                selenium---->python/java/.net

    Deprecation Waring----->??????
        order to new
        selenium3.x to selenium4.x---->error or Deprecation

    python2----->
    python3 ----->
    dict----> 3---> order dict
    dict---> 2---> not order

    rawinput()

    input()

    range()----->

    xrange()----> object ref of iterable

    double

    int,float




Selenium---->
1 open source Automation functional Testing tool
2 Framewrok ----> web application----REQ-RESP
        web application----> web server
                    AWS---amazon web service
                    cloud
                    MVT---> Django/Fask
3 Use for the browser----> webdriver
4 selenium+python---->binding to provide api to the application
selenium---api
5 API to access selenium webdriver to the browser--->
6 Web applications--->
        but not angular js or react application-----> usede Protractor
        but not desktop application-----> sikuli
                                ----> selenium2
        POPUP----> selenium webapplication******
        URL or URI
        https


Selenium Components---->
1 SELENIUM IDE----> Integrated Developement Env
                ----> Record and Run  TC
                every action on application recorded and run the action(event,task perform by hardware)
                ----> only installed on Firefox
                ----> bydefault ---> HTML formate
                HTML----> user req----> XML
2 Selenium RC----> remote control
            at a time only 1 browser
                    chrome , firefox
            selenium 1.X
            web server is resp to open all the browsers
            but selenium1 will only one browser at time
            it act selenium as API
3 Selemium webdriver---->***
        work multiple ----> no limit
        adavance version of RC
         parallel execution---> save execution time
         compartiable for all OS

4 Selenium GRID---->
        at a time only 5 browsers
        parallel execution---> save execution time
        compartiable for all OS

5 SEKENDROID and APPIUM---->
                To automate Mobile Application


API---->
UI--->***

Features of Selenium---->
Open source, all OS, All browsers
combination of Tool
but it not the compon---> protactor,sikuli, SEKENDROID and APPIUM
Easy to understand, implement
Reduced the Test Execution
parallel test execution
suport the multiple lamnguage----> python,java,.net,c++,c#
OS----> windows families 7,8,9,10
        IOS
        MAC
        Linux/ubuntu/kalios
        centOS
browsers----> chrome,firefox,IE,opera,Edge,Safari
Diadvace---->
            No desktop application automation--->
                    Sikuli used
            Maintance is hevy
            Angular JS---->
                    protactor tool

            No reporting ---->pytest
                    inbuilt
                SS---->
            Image Testing,video testing--->No
            Captcha-----> No
            bar code ----> No
            payment ---> No

get----> instance ----> obj.get(url)
maximize_window()---> browser maxim
close()----> automation thro --- browser close


import sys
import time
from selenium import webdriver
import chromedriver_autoinstaller
chromedriver_autoinstaller.install()
driver=webdriver.Chrome()
driver.get('https://www.selenium.dev/about/')
time.sleep(5)
if driver.title=='About Selenium | Selenium':
    print('pass')
else:
    print('failed')
driver.close()
sys.exit(0)
driver=webdriver.Chrome('E:\\sel_driver\\chromedriver.exe')
driver.get('https://www.selenium.dev/about/')