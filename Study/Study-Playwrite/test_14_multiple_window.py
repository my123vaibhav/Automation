from playwright.sync_api import sync_playwright

def test_multiple_windows():
    with sync_playwright() as p:
        ctx = p.chromium.launch(headless=True).new_context()
        page = ctx.new_page()
        page.goto("https://the-internet.herokuapp.com/windows")
        with ctx.expect_page() as ninfo:
            page.click("text=Click Here")
        newp = ninfo.value
        assert "New Window" in newp.locator("h3").text_content()
        newp.close()
        assert "Multiple Windows" in page.locator("h3").text_content()
