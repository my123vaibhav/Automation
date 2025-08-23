from pages.base_page import BasePage
from utils.config import BASE_URL

class LoginPage(BasePage):
    URL = f"{BASE_URL}/login"
    USERNAME = "#username"
    PASSWORD = "#password"
    LOGIN_BTN = "button[type='submit']"
    FLASH = "#flash"

    def load(self):
        self.navigate(self.URL)

    def login(self, user, password):
        self.fill(self.USERNAME, user)
        self.fill(self.PASSWORD, password)
        self.click(self.LOGIN_BTN)

    def get_flash_message(self):
        return self.get_text(self.FLASH)
