from playwright.sync_api import sync_playwright

def test_form_auth():
    with sync_playwright() as p:
        page = p.chromium.launch(headless=True).new_page()
        page.goto("https://the-internet.herokuapp.com/login")
        page.fill("input#username", "tomsmith")
        page.fill("input#password", "SuperSecretPassword!")
        page.click("button[type='submit']")
        assert "Secure Area" in page.locator("h2").text_content()
