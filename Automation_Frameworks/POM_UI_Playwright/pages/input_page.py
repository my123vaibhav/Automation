from pages.base_page import BasePage
from utils.config import BASE_URL

class InputPage(BasePage):
    URL = f"{BASE_URL}/inputs"
    INPUT = "input[type='number']"

    def load(self):
        self.navigate(self.URL)

    def enter_number(self, value):
        self.fill(self.INPUT, str(value))

    def get_value(self):
        return self.page.locator(self.INPUT).input_value()
