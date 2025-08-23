from playwright.sync_api import sync_playwright

def test_add_remove():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False,slow_mo=400)
        page = browser.new_page()
        page.goto("https://the-internet.herokuapp.com/add_remove_elements/")
        add_btn = page.get_by_text("Add Element")
        add_btn.click()
        add_btn.click()
        delete_buttons = page.get_by_text("Delete")
        assert delete_buttons.count() == 2

        delete_buttons.first.click()
        assert delete_buttons.count() == 1
        browser.close()
