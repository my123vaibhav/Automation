import time

from pages.key_presses_page import KeyPressesPage

def test_key_presses(browser):
    kp = KeyPressesPage(browser)
    kp.load()
    kp.press_key("A")
    assert "A" in kp.get_result()
    kp.press_key("Tab")
    assert "TAB" in kp.get_result()
