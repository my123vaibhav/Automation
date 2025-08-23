from pages.context_menu_page import ContextMenuPage

def test_context_menu(browser):
    cm_page = ContextMenuPage(browser)
    cm_page.load()
    alert_text = cm_page.get_alert_text()
    assert "You selected a context menu" in alert_text
