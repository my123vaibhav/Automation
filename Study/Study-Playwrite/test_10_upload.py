from pathlib import Path
from playwright.sync_api import sync_playwright

def test_file_upload():
    test_file = Path("test_upload.txt")
    test_file.write_text("Hello")
    with sync_playwright() as p:
        page = p.chromium.launch(headless=True).new_page()
        page.goto("https://the-internet.herokuapp.com/upload")
        page.locator("input[type='file']").set_input_files(str(test_file))
        page.locator("input#file-submit").click()
        assert page.locator("#uploaded-files").text_content().strip() == "test_upload.txt"
