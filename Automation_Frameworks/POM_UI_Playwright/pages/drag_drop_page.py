from pages.base_page import BasePage
from utils.config import BASE_URL

class DragDropPage(BasePage):
    URL = f"{BASE_URL}/drag_and_drop"
    COLUMN_A = "#column-a"
    COLUMN_B = "#column-b"

    def load(self):
        self.navigate(self.URL)

    def drag_a_to_b(self):
        self.page.locator(self.COLUMN_A).drag_to(self.page.locator(self.COLUMN_B))

    def get_a_text(self):
        return self.get_text(self.COLUMN_A)

    def get_b_text(self):
        return self.get_text(self.COLUMN_B)
