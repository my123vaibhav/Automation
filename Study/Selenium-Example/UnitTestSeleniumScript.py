import unittest
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys


class InputFormsCheck(unittest.TestCase):

    # Opening browser.
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\Users\nishant.narwade\PycharmProjects\pythonSeleniumStudy\All_Browser\chromedriver2.exe")

    # Testing Single Input Field.
    def test_singleInputField(self):

        driver = self.driver
        # driver=webdriver.firefox()
        # driver=webdriver.ie()
        # maximize the window size
        driver.maximize_window()
        # navigate to the url
        driver.get("https://www.google.com/")
        # identify the Google search text box and enter the value
        driver.find_element_by_name("q").send_keys("javatpoint")
        time.sleep(3)
        # click on the Google search button
        driver.find_element_by_name("btnK").send_keys(Keys.ENTER)
        time.sleep(3)

    # Closing the browser.
    def tearDown(self):
        self.driver.close()


# This line sets the variable “__name__” to have a value “__main__”.
# If this file is being imported from another module then “__name__” will be set to the other module's name.
if __name__ == "__main__":
    unittest.main()