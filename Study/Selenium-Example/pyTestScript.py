import pytest
from selenium import webdriver


@pytest.fixture()
def setup(self):
    print("initiating chrome driver")
    self.driver = webdriver.Chrome(
        executable_path=r"C:\Users\nishant.narwade\PycharmProjects\pythonSeleniumStudy\All_Browser\chromedriver2.exe")
    self.driver.get("http://seleniumeasy.com/test")
    self.driver.maximize_window()

    yield self.driver
    self.driver.close()


@pytest.mark.usefixtures("setup")
class TestExample:
    def test_title(self):
        self.driver = self.driver;
        print("Verify title...")
        assert "Selenium Easy" in self.driver.title

    def test_content_text(self):
        print("Verify content on the page...")
        centerText = self.driver.find_element_by_css_selector('.tab-content .text-center').text
        assert "WELCOME TO SELENIUM EASY DEMO" == centerText
