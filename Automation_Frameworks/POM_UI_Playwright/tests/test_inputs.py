from pages.input_page import InputPage

def test_input_numbers(browser):
    ip = InputPage(browser)
    ip.load()
    ip.enter_number(12345)
    assert ip.get_value() == "12345"
