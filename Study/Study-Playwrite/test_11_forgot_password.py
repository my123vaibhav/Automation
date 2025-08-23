from playwright.sync_api import sync_playwright

def test_forgot_password():
    with sync_playwright() as p:
        page = p.chromium.launch(headless=True).new_page()
        page.goto("https://the-internet.herokuapp.com/forgot_password")
        page.fill("input#email", "user@example.com")
        page.click("button#form_submit")
        assert "internal only" in page.locator("div#content").text_content()
