from pages.base_page import BasePage
from utils.config import BASE_URL
import os

class DownloadPage(BasePage):
    URL = f"{BASE_URL}/download"
    FILE_LINK = "div.example a"

    def load(self):
        self.navigate(self.URL)

    def download_file(self):
        with self.page.expect_download() as download_info:
            self.page.locator(self.FILE_LINK).first.click()
        download = download_info.value
        path = download.path()
        return os.path.basename(path)
