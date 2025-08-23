from pages.download_page import DownloadPage

def test_file_download(browser, tmp_path):
    dl_page = DownloadPage(browser)
    dl_page.load()
    filename = dl_page.download_file()
    assert filename is not None
