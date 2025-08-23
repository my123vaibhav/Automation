import pytest

from pages.frames_page import FramesPage

@pytest.mark.skip(reason="not implemented")
def test_iframe_edit(browser):
    fp = FramesPage(browser)
    fp.load()
    fp.enter_text_in_iframe("Hello Playwright")
    assert "Hello Playwright" in fp.get_text_from_iframe()

