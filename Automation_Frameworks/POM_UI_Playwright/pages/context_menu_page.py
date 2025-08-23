from pages.base_page import BasePage
from utils.config import BASE_URL

class ContextMenuPage(BasePage):
    URL = f"{BASE_URL}/context_menu"
    HOTSPOT = "#hot-spot"

    def load(self):
        self.navigate(self.URL)

    def right_click(self):
        self.page.locator(self.HOTSPOT).click(button="right")

    def get_alert_text(self):
        dialog_text = None

        def handle_dialog(dialog):
            nonlocal dialog_text
            dialog_text = dialog.message
            dialog.accept()

        self.page.once("dialog", handle_dialog)
        self.right_click()
        return dialog_text
