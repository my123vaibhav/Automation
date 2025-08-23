from playwright.sync_api import sync_playwright

def test_key_presses():
    with sync_playwright() as p:
        page = p.chromium.launch(headless=True).new_page()
        page.goto("https://the-internet.herokuapp.com/key_presses")
        page.press("body", "A")
        assert "You entered: A" in page.locator("#result").text_content()
