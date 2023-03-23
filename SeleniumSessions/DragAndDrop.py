from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By

service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.delete_all_cookies()
driver.get('https://jqueryui.com/resources/demos/droppable/default.html')

'''drag and drop'''
source = driver.find_element(By.ID, 'draggable')
target = driver.find_element(By.ID, 'droppable')

act_chains = ActionChains(driver)
# act_chains.drag_and_drop(source,target).perform()

act_chains \
    .click_and_hold(source) \
    .move_to_element(target) \
    .release() \
    .perform()
driver.quit()
print("Test case completed")
