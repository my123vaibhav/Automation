from pages.dropdown_page import DropdownPage

def test_dropdown(browser):
    dd_page = DropdownPage(browser)
    dd_page.load()
    dd_page.select_option("1")
    assert dd_page.get_selected_value() == "1"
