from playwright.sync_api import sync_playwright

def test_drag_drop():
    with sync_playwright() as p:
        page = p.chromium.launch(headless=True).new_page()
        page.goto("https://the-internet.herokuapp.com/drag_and_drop")
        page.drag_and_drop("#column-a", "#column-b")
        assert page.locator("#column-a header").text_content() == "B"
