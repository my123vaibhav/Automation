from pages.base_page import BasePage
from utils.config import BASE_URL

class KeyPressesPage(BasePage):
    URL = "https://the-internet.herokuapp.com/key_presses"
    INPUT = "#target"
    RESULT = "#result"

    def load(self):
        self.page.goto(self.URL)

    def press_key(self, key):
        self.page.locator(self.INPUT).press(key)

    def get_result(self):
        return self.page.locator(self.RESULT).inner_text()
