from playwright.sync_api import expect

from config.base import BASE_URL


class BasePage:
    def __init__(self, page):
        self.page = page

    def open_page(self):
        self.page.goto(BASE_URL)

    def expect_to_have_url(self, url_sub: str):
        expect(self.page).to_have_url(BASE_URL)
