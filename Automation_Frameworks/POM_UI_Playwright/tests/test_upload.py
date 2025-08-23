from pages.upload_page import UploadPage
import os

def test_file_upload(browser, tmp_path):
    test_file = tmp_path / "sample.txt"
    test_file.write_text("hello playwright")

    up_page = UploadPage(browser)
    up_page.load()
    up_page.upload_file(str(test_file))
    assert "File Uploaded!" in up_page.get_uploaded_message()
