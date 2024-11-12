from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_eight_components():
    driver = webdriver.Chrome("D:\\pythonProject\\API-Backend-Automation\\ALL-EXE\\chromedriver.exe")

    driver.get("https://www.selenium.dev/selenium/web/web-form.html")

    title = driver.title
    #driver.get_screenshot_as_png()
    print("Take a screenshot")
    driver.get_screenshot_as_file('./Screenshots/foo.png')
    assert title == "Web form"

    driver.implicitly_wait(0.5)

    text_box = driver.find_element(by=By.NAME, value="my-text")
    submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")


    text_box.send_keys("Selenium")
    submit_button.click()

    message = driver.find_element(by=By.ID, value="message")
    value = message.text
    assert value == "Received!"

    driver.quit()
    print("test cases completed -pass")


test_eight_components()
