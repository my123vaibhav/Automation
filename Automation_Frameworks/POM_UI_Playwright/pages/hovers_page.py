from pages.base_page import BasePage
from utils.config import BASE_URL

class HoversPage(BasePage):
    URL = f"{BASE_URL}/hovers"
    AVATAR = ".figure"
    CAPTION = ".figcaption"

    def load(self):
        self.navigate(self.URL)

    def hover_avatar(self, index=0):
        avatar = self.page.locator(self.AVATAR).nth(index)
        avatar.hover()
        return avatar.locator(self.CAPTION).inner_text()
