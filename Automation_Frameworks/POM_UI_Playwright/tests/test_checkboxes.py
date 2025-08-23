from pages.checkbox_page import CheckboxPage

def test_checkboxes(browser):
    cb_page = CheckboxPage(browser)
    cb_page.load()

    cb_page.check_first()
    assert cb_page.is_first_checked()

    cb_page.uncheck_second()
    assert not cb_page.is_second_checked()
