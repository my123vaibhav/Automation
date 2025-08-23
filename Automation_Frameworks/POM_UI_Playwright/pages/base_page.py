class BasePage:
    def __init__(self, page):
        self.page = page

    def navigate(self, url):
        self.page.goto(url)

    def click(self, locator):
        self.page.locator(locator).click()

    def fill(self, locator, text):
        self.page.locator(locator).fill(text)

    def get_text(self, locator):
        return self.page.locator(locator).text_content()

    def is_visible(self, locator):
        return self.page.locator(locator).is_visible()

    def is_checked(self, locator):
        return self.page.locator(locator).is_checked()

    def select_option(self, locator, value):
        self.page.select_option(locator, value=value)
