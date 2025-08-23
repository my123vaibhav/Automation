from pages.windows_page import WindowsPage

def test_new_window(browser):
    wp = WindowsPage(browser)
    wp.load()
    new_tab = wp.open_new_window()
    new_tab.wait_for_load_state()
    assert "New Window" in new_tab.content()
