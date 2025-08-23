from pages.base_page import BasePage
from utils.config import BASE_URL

class AuthPage(BasePage):
    URL = f"https://admin:admin@the-internet.herokuapp.com/basic_auth"
    SUCCESS_TEXT = "p"

    def load(self):
        self.navigate(self.URL)

    def get_message(self):
        return self.get_text(self.SUCCESS_TEXT)
