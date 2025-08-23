from playwright.sync_api import sync_playwright

def test_dropdown_selection():
    with sync_playwright() as p:
        page = p.chromium.launch(headless=True).new_page()
        page.goto("https://the-internet.herokuapp.com/dropdown")
        page.select_option("select#dropdown", label="Option 1")
        assert page.locator("select#dropdown").input_value() == "1"
        page.select_option("select#dropdown", value="2")
        assert page.locator("select#dropdown").input_value() == "2"
