from pathlib import Path
from playwright.sync_api import sync_playwright

def test_file_download():
    dl_dir = Path.cwd() / "downloads"
    dl_dir.mkdir(exist_ok=True)
    with sync_playwright() as p:
        ctx = p.chromium.launch(headless=True).new_context(accept_downloads=True)
        page = ctx.new_page()
        page.goto("https://the-internet.herokuapp.com/download")

        with page.expect_download() as dinf:
            page.click("text=some-file.txt")
        dl = dinf.value
        path = dl.save_as(str(dl_dir / dl.suggested_filename))
        assert Path(path).exists()
