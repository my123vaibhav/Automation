from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
print("sample test case started")
driver = webdriver.Chrome(executable_path=r"C:\Users\nishant.narwade\PycharmProjects\pythonSeleniumStudy\All_Browser\chromedriver3.exe")
#driver = webdriver.Ie(executable_path=r"C:\Users\nishant.narwade\PycharmProjects\pythonSeleniumStudy\All_Browser\IEDriverServer.exe")
#driver = webdriver.Edge(executable_path=r"C:\Users\nishant.narwade\PycharmProjects\pythonSeleniumStudy\All_Browser\msedgedriver.exe")
#driver = webdriver.Ie(executable_path=r".//All_Browser//chromedriver.exe")
#driver=webdriver.chrome();
#driver=webdriver.ie()
#maximize the window size


driver.maximize_window()
#navigate to the url
driver.get("https://www.google.com/")
#identify the Google search text box and enter the value
driver.find_element_by_name("q").send_keys("javatpoint")
time.sleep(3)
#click on the Google search button
driver.find_element_by_name("btnK").send_keys(Keys.ENTER)
time.sleep(3)
#close the browser
driver.close()
print("sample test case successfully completed")