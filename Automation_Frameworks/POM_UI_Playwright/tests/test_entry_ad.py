import pytest

from pages.entry_ad_page import EntryAdPage

@pytest.mark.skip(reason="not implemented")
def test_entry_ad(browser):
    entry_page = EntryAdPage(browser)
    entry_page.load()

    # Try waiting for modal
    if not entry_page.is_modal_visible(timeout=5000):
        entry_page.force_show_modal()

    assert entry_page.is_modal_visible(timeout=5000), "Modal should be visible after load or re-enable"

    entry_page.close_modal()
    assert not entry_page.is_modal_visible(), "Modal should be closed after clicking Close"
