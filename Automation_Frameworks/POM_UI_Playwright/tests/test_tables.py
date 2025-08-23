from pages.tables_page import TablesPage

def test_tables(browser):
    tbl_page = TablesPage(browser)
    tbl_page.load()
    data = tbl_page.get_all_table_data()
    assert len(data) > 0
    assert "Smith" in str(data)
