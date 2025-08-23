from pages.alerts_page import AlertsPage


def test_js_alert(browser):
    page = AlertsPage(browser)
    page.load()
    page.trigger_alert()
    assert "You successfully clicked an alert" in page.get_result()


def test_js_confirm(browser):
    page = AlertsPage(browser)
    page.load()
    page.trigger_confirm(accept=False)
    assert "Cancel" in page.get_result()


def test_js_prompt(browser):
    page = AlertsPage(browser)
    page.load()
    page.trigger_prompt("Playwright")
    assert "Playwright" in page.get_result()
