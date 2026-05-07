from playwright.sync_api import expect

from pages.base_page import BasePage


class HomePage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.btn_login = self.page.get_by_text("Login or register")
        self.btn_add_to_cart = self.page.get_by_title("Add to Cart")
        self.product_name = self.page.locator(".prdocutname")
        self.added_to_cart = self.page.get_by_title("Added to cart")

    def click_btn_login(self):
        self.btn_login.click()

    def add_product_to_cart(self, index):
        self.btn_add_to_cart.nth(index).click()
        product = (self.product_name.nth(index)).inner_text()
        print(f'Товар "{product}" добавлен в корзину')

    def check_added_to_cart(self, index):
        expect(self.added_to_cart.nth(index)).to_be_visible()

    def go_to_cart_page(self):
        self.added_to_cart.click()
