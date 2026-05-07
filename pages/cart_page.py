from playwright.sync_api import expect
from pages.base_page import BasePage


class CartPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.remove_item = self.page.locator(".btn.btn-sm.btn-default")
        self.txt_empty_cart = self.page.locator(".contentpanel")

    def del_item_in_cart(self):
        self.remove_item.click()

    def expect_to_empty_cart(self, text):
        expect(self.txt_empty_cart).to_contain_text(text)