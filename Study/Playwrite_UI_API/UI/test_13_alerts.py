from playwright.sync_api import sync_playwright

def test_js_alerts():
    with sync_playwright() as p:
        page = p.chromium.launch(headless=True).new_page()
        page.goto("https://the-internet.herokuapp.com/javascript_alerts")

        # Alert
        msg = None
        page.once("dialog", lambda d: (globals().update(msg=d.message), d.accept()))
        page.click("text=Click for JS Alert")
        assert msg == "I am a JS Alert"
        assert "You successfully clicked an alert" in page.locator("#result").text_content()

        # Confirm OK
        page.once("dialog", lambda d: (globals().update(msg=d.message), d.accept()))
        page.click("text=Click for JS Confirm")
        assert "You clicked: Ok" in page.locator("#result").text_content()

        # Prompt
        input_msg = "Hello!"
        page.once("dialog", lambda d: (globals().update(msg=d.message), d.accept(input_msg)))
        page.click("text=Click for JS Prompt")
        assert f"You entered: {input_msg}" in page.locator("#result").text_content()
