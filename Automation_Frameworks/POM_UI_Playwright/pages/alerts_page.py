from pages.base_page import BasePage
from utils.config import BASE_URL


class AlertsPage(BasePage):
    URL = f"{BASE_URL}/javascript_alerts"

    ALERT_BTN = "button[onclick='jsAlert()']"
    CONFIRM_BTN = "button[onclick='jsConfirm()']"
    PROMPT_BTN = "button[onclick='jsPrompt()']"
    RESULT = "#result"

    def load(self):
        self.navigate(self.URL)

    def trigger_alert(self):
        def handle_dialog(dialog):
            dialog.accept()

        self.page.once("dialog", handle_dialog)
        self.click(self.ALERT_BTN)

    def trigger_confirm(self, accept=True):
        def handle_dialog(dialog):
            if accept:
                dialog.accept()
            else:
                dialog.dismiss()

        self.page.once("dialog", handle_dialog)
        self.click(self.CONFIRM_BTN)

    def trigger_prompt(self, text):
        def handle_dialog(dialog):
            dialog.accept(text)

        self.page.once("dialog", handle_dialog)
        self.click(self.PROMPT_BTN)

    def get_result(self):
        return self.get_text(self.RESULT)
