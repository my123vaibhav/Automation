from playwright.sync_api import sync_playwright

def test_capture_all_table1():
    with sync_playwright() as p:
        page = p.chromium.launch(headless=True).new_page()
        page.goto("https://the-internet.herokuapp.com/tables")
        table = page.locator("table#table1")
        headers = [h.text_content().strip() for h in table.locator("thead th").all()]
        rows = []
        for row in table.locator("tbody tr").all():
            cells = [c.text_content().strip() for c in row.locator("td").all()]
            rows.append(dict(zip(headers, cells)))
        print(rows)
