from playwright.sync_api import sync_playwright

def test_numeric_input():
    with sync_playwright() as p:
        page = p.chromium.launch(headless=True).new_page()
        page.goto("https://the-internet.herokuapp.com/inputs")
        inp = page.locator("input[type='number']")
        inp.fill("")
        inp.type("50")
        assert inp.input_value() == "50"
        inp.press("ArrowUp")
        assert int(inp.input_value()) == 51
