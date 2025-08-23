from pages.auth_page import AuthPage

def test_basic_auth(browser):
    page = AuthPage(browser)
    page.load()
    msg = page.get_message()
    assert "Congratulations" in msg
