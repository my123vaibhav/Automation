from pages.login_page import LoginPage

def test_valid_login(browser):
    lp = LoginPage(browser)
    lp.load()
    lp.login("tomsmith", "SuperSecretPassword!")
    assert "You logged into a secure area!" in lp.get_flash_message()

def test_invalid_login(browser):
    lp = LoginPage(browser)
    lp.load()
    lp.login("wrong", "wrong")
    assert "Your username is invalid!" in lp.get_flash_message()
