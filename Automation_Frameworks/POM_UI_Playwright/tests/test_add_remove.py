from pages.add_remove_page import AddRemovePage
from utils.logger import *

logger = get_logger(__name__)

def test_add_and_remove(browser):
    page = AddRemovePage(browser)
    logger.info('page is opening')
    page.load()
    page.add_element()
    assert page.is_delete_visible()
    page.delete_element()
