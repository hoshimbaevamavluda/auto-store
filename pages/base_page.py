from playwright.sync_api import expect


class BasePage:
    def __init__(self, page):
        self.page = page

    def open_page(self, url):
        self.page.goto(url)

    def expect_to_have_url(self, url_sub: str):
        expect(self.page).to_have_url(url_sub)
