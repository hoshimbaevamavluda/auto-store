from playwright.sync_api import expect
from pages.base_page import BasePage


class CartPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.remove_item = self.page.locator(".btn.btn-sm.btn-default")
        self.txt_empty_cart = self.page.locator(".contentpanel")
        self.item_quantity = self.page.locator("#cart_quantity50")

    def del_item_in_cart(self):
        self.remove_item.click()

    def expect_to_empty_cart(self, text):
        expect(self.txt_empty_cart).to_contain_text(text)

    def change_quantity(self, quantity):
        self.item_quantity.fill(quantity)
        expect(self.item_quantity).to_have_value(quantity)
