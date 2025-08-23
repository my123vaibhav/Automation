from playwright.sync_api import sync_playwright

def test_checkboxes():
    with sync_playwright() as p:
        page = p.chromium.launch(headless=False,slow_mo=200).new_page()
        page.goto("https://the-internet.herokuapp.com/checkboxes")
        c1, c2 = page.locator("input[type='checkbox']").nth(0), page.locator("input[type='checkbox']").nth(1)

        c1.check()
        assert c1.is_checked()
        c2.uncheck()
        assert not c2.is_checked()
