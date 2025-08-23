from playwright.sync_api import sync_playwright

def test_context_menu_alert():
    with sync_playwright() as p:
        page = p.chromium.launch(headless=False,slow_mo=200).new_page()
        page.goto("https://the-internet.herokuapp.com/context_menu")

        msg = None
        def handler(dialog):
            nonlocal msg
            msg = dialog.message
            dialog.accept()
        page.on("dialog", handler)

        page.click("#hot-spot", button="right")
        assert msg == "You selected a context menu"
