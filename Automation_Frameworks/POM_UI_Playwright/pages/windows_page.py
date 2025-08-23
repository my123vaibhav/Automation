from pages.base_page import BasePage
from utils.config import BASE_URL

class WindowsPage(BasePage):
    URL = f"{BASE_URL}/windows"
    CLICK_LINK = "a[href='/windows/new']"

    def load(self):
        self.navigate(self.URL)

    def open_new_window(self):
        with self.page.context.expect_page() as new_page_info:
            self.click(self.CLICK_LINK)
        return new_page_info.value
