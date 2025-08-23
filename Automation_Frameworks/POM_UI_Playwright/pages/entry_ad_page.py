from pages.base_page import BasePage
from utils.config import BASE_URL

class EntryAdPage(BasePage):
    URL = f"{BASE_URL}/entry_ad"

    MODAL = "#modal"
    CLOSE_BTN = "text=Close"
    REENABLE_LINK = "a#restart-ad"   # the "click here" link

    def load(self):
        # reset site storage so modal appears
        self.page.add_init_script("window.localStorage.clear();")
        self.navigate(self.URL)

    def is_modal_visible(self, timeout: int = 5000):
        try:
            return self.page.locator(self.MODAL).is_visible(timeout=timeout)
        except:
            return False

    def close_modal(self):
        if self.is_modal_visible():
            self.click(self.CLOSE_BTN)

    def force_show_modal(self):
        # sometimes modal doesn’t show, so click "click here" link
        self.click(self.REENABLE_LINK)

