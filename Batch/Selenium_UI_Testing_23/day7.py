import time
#ActionChains
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
chromedriver_autoinstaller.install()

drive=webdriver.Chrome()
drive.maximize_window()
drive.get('http://seleniumpractise.blogspot.com/2016/08/how-to-perform-mouse-hover-in-selenium.html')

at=drive.find_element(By.XPATH,"//button[normalize-space()='Automation Tools']")
act=ActionChains(drive)
act.move_to_element(at).perform()
time.sleep(3)
drive.find_element(By.XPATH,"//a[text()='TestNG']").click()
time.sleep(3)
drive.close()

import sys
sys.exit(0)
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
chromedriver_autoinstaller.install()

driver=webdriver.Chrome()
driver.maximize_window()
driver.get('http://seleniumpractise.blogspot.com/2016/08/how-to-perform-mouse-hover-in-selenium.html')
time.sleep(2)
automationTool=driver.find_element(By.XPATH,"//button[normalize-space()='Automation Tools']")
act=ActionChains(driver)
act.move_to_element(automationTool).pause(30).click(driver.find_element(By.XPATH,"//a[text()='Appium']")).perform()


import sys
sys.exit(0)
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
chromedriver_autoinstaller.install()

driver=webdriver.Chrome()
driver.maximize_window()
driver.get('http://seleniumpractise.blogspot.com/2016/08/how-to-perform-mouse-hover-in-selenium.html')
time.sleep(2)
automationTool=driver.find_element(By.XPATH,"//button[normalize-space()='Automation Tools']")
act=ActionChains(driver)
act.move_to_element(automationTool).perform()
time.sleep(2)
driver.find_element(By.XPATH,"//button[normalize-space()='Automation Tools']").click()
time.sleep(2)
print(driver.current_url)