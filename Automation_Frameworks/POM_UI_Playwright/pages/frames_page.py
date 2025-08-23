from pages.base_page import BasePage
from utils.config import BASE_URL

class FramesPage(BasePage):
    URL = f"{BASE_URL}/iframe"

    IFRAME = "#mce_0_ifr"
    EDITOR = "#tinymce"

    def load(self):
        self.navigate(self.URL)

    def enter_text_in_iframe(self, text: str):
        frame = self.page.frame_locator(self.IFRAME)
        editor = frame.locator(self.EDITOR)

        # Ensure it's ready and editable
        editor.wait_for(state="visible")

        # Clear old text (Ctrl+A + Delete)
        editor.click()
        editor.press("Control+A")
        editor.press("Delete")

        # Type new text
        editor.type(text)

    def get_text_from_iframe(self):
        frame = self.page.frame_locator(self.IFRAME)
        return frame.locator(self.EDITOR).inner_text()
