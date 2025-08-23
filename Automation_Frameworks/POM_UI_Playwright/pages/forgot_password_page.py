from pages.base_page import BasePage
from utils.config import BASE_URL

class ForgotPasswordPage(BasePage):
    URL = f"{BASE_URL}/forgot_password"
    EMAIL_INPUT = "#email"
    RETRIEVE_BTN = "#form_submit"
    CONFIRM_TEXT = "#content"

    def load(self):
        self.navigate(self.URL)

    def submit_email(self, email):
        self.fill(self.EMAIL_INPUT, email)
        self.click(self.RETRIEVE_BTN)

    def get_message(self):
        return self.get_text(self.CONFIRM_TEXT)
