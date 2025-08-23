from pages.base_page import BasePage
from utils.config import BASE_URL


class DropdownPage(BasePage):
    URL = f"{BASE_URL}/dropdown"
    DROPDOWN = "#dropdown"

    def load(self):
        self.navigate(self.URL)

    def select_option(self, value: str):
        """Select option by value ('1' or '2')."""
        self.page.select_option(self.DROPDOWN, value=value)

    def get_selected_value(self) -> str:
        """Return the currently selected option value."""
        return self.page.locator(self.DROPDOWN).input_value()
