from pages.base_page import BasePage
from utils.config import BASE_URL

class CheckboxPage(BasePage):
    URL = f"{BASE_URL}/checkboxes"
    CHECKBOX = "input[type='checkbox']"

    def load(self):
        self.navigate(self.URL)

    def check_first(self):
        self.page.locator(self.CHECKBOX).nth(0).check()

    def uncheck_second(self):
        self.page.locator(self.CHECKBOX).nth(1).uncheck()

    def is_first_checked(self):
        return self.page.locator(self.CHECKBOX).nth(0).is_checked()

    def is_second_checked(self):
        return self.page.locator(self.CHECKBOX).nth(1).is_checked()
