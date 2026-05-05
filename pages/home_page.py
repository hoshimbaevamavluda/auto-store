from playwright.sync_api import expect

from pages.base_page import BasePage


class HomePage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.btn_login = self.page.get_by_text("Login or register")
        self.btn_add_to_cart = self.page.locator(".productcart").first
        self.added_to_cart = self.page.get_by_title("Added to cart").first

    def click_btn_login(self):
        self.btn_login.click()

    def add_to_cart(self):
        self.btn_add_to_cart.click()

    def check_added_to_cart(self):
        expect(self.added_to_cart).to_be_visible()


