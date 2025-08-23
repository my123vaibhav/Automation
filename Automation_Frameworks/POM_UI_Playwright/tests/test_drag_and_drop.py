from pages.drag_drop_page import DragDropPage

def test_drag_and_drop(browser):
    dd_page = DragDropPage(browser)
    dd_page.load()
    dd_page.drag_a_to_b()
    assert dd_page.get_a_text() == "B"
    assert dd_page.get_b_text() == "A"
