from pages.base_page import BasePage
from utils.config import BASE_URL

class TablesPage(BasePage):
    URL = f"{BASE_URL}/tables"
    TABLE = "#table1"

    def load(self):
        self.navigate(self.URL)

    def get_all_table_data(self):
        rows = self.page.locator(f"{self.TABLE} tbody tr")
        data = []
        for i in range(rows.count()):
            cols = rows.nth(i).locator("td")
            row_data = [cols.nth(j).inner_text() for j in range(cols.count())]
            data.append(row_data)
        return data
