from pages.base_page import BasePage
from utils.config import BASE_URL

class AddRemovePage(BasePage):
    URL = f"{BASE_URL}/add_remove_elements/"
    ADD_BTN = "button[onclick='addElement()']"
    DELETE_BTN = "button.added-manually"

    def load(self):
        self.navigate(self.URL)

    def add_element(self):
        self.click(self.ADD_BTN)

    def delete_element(self):
        self.click(self.DELETE_BTN)

    def is_delete_visible(self):
        return self.is_visible(self.DELETE_BTN)
