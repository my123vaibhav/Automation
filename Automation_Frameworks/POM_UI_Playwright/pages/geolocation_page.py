from pages.base_page import BasePage
from utils.config import BASE_URL

class GeolocationPage(BasePage):
    URL = f"{BASE_URL}/geolocation"
    GEO_BTN = "button[onclick='getLocation()']"

    def load(self):
        self.navigate(self.URL)

    def get_location(self):
        self.click(self.GEO_BTN)
        latitude = self.page.locator("#lat-value").inner_text()
        longitude = self.page.locator("#long-value").inner_text()
        return latitude, longitude
