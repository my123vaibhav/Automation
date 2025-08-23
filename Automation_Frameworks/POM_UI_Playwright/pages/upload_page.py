from pages.base_page import BasePage
from utils.config import BASE_URL

class UploadPage(BasePage):
    URL = f"{BASE_URL}/upload"
    FILE_INPUT = "#file-upload"
    UPLOAD_BTN = "#file-submit"
    UPLOADED_TEXT = "h3"

    def load(self):
        self.navigate(self.URL)

    def upload_file(self, file_path):
        self.page.set_input_files(self.FILE_INPUT, file_path)
        self.click(self.UPLOAD_BTN)

    def get_uploaded_message(self):
        return self.get_text(self.UPLOADED_TEXT)
