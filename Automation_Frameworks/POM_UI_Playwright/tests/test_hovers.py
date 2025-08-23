from pages.hovers_page import HoversPage

def test_hover_avatars(browser):
    hover_page = HoversPage(browser)
    hover_page.load()
    text = hover_page.hover_avatar(0)
    assert "name:" in text.lower()
