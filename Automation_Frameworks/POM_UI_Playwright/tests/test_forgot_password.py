from pages.forgot_password_page import ForgotPasswordPage
import pytest


@pytest.mark.skip(reason="not implemented")
def test_forgot_password(browser):
    fp_page = ForgotPasswordPage(browser)
    fp_page.load()
    fp_page.submit_email("test@example.com")
    msg = fp_page.get_message()
    assert "Your e-mail's been sent!" in msg
