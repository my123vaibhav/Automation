from playwright.sync_api import sync_playwright

def test_entry_ad():
    with sync_playwright() as p:
        page = p.chromium.launch(headless=True).new_page()
        page.goto("https://the-internet.herokuapp.com/entry_ad")
        assert page.locator("#modal").is_visible()
        page.locator(".modal-footer p").click()
        assert not page.locator("#modal").is_visible()
        page.locator("text=click here").click()
        assert page.locator("#modal").is_visible()
