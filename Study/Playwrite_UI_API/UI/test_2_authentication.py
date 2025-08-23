from playwright.sync_api import sync_playwright

def test_basic_auth():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False,slow_mo=400)
        context = browser.new_context(http_credentials={"username": "admin", "password": "admin"})
        page = context.new_page()
        page.goto("https://the-internet.herokuapp.com/basic_auth")
        assert "Congratulations" in page.content()
        browser.close()
