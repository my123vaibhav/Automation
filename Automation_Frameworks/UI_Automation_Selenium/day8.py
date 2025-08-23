import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
#//div[@id='column-b']
#//div[@id='column-a']
driver=webdriver.Firefox()
driver.get('https://stepupandlearn.in/wp-content/UI/drag_and_drop.html')
source=driver.find_element(By.XPATH,"//div[@id='column-a']")
destination=driver.find_element(By.XPATH,"//div[@id='column-b']")

ActionChains(driver).drag_and_drop(source,destination).perform()


time.sleep(3)



driver.quit()






#
# driver=webdriver.Firefox()
#
# driver.get("https://demo.automationtesting.in/Windows.html")
#
# driver.implicitly_wait(3)
#
# element=driver.find_element(By.XPATH,"//*[@id='Tabbed']/a/button")
#
# element.click()
#
# l1=driver.window_handles
#
#
# for i in l1:
#     print(driver.title)
#     driver.switch_to.window(i)
#     print(driver.title)



driver.quit()