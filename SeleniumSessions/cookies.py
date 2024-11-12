from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
import time

service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.delete_all_cookies()
driver.implicitly_wait(10)

driver.get('https://reddit.com')
print(driver.get_cookies())

driver.add_cookie({"name":"python","domain":"reddit.com","value":"python"})
print(driver.get_cookies())
print(driver.get_cookie('domain'))

driver.delete_all_cookies()

print(driver.get_cookies())
#driver.get_screenshot_as_file("screenshot.png")

S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
driver.set_window_size(S('Width'),S('Height')) # May need manual adjustment
driver.find_element(By.TAG_NAME,'body').screenshot('web_screenshot.png')


# cookies = driver.get_cookies()
# for cook in cookies:
#     print(cook)


driver.quit()