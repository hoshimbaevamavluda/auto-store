import allure
from playwright.sync_api import expect

from pages.base_page import BasePage


class HomePage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.btn_login = self.page.get_by_text("Login or register")
        self.btn_add_to_cart = self.page.get_by_title("Add to Cart")
        self.product_name = self.page.locator(".prdocutname")
        self.cart_in_menu = self.page.locator('.dropdown[data-id="menu_cart"]').nth(1)
        self.cart_in_header = self.page.locator('.dropdown[data-id="menu_cart"]').first
        self.added_to_cart = self.page.get_by_title("Added to cart")
        self.popup_close = self.page.locator('.popup-close')
        self.home_btn = self.page.locator(".active.menu_home")

    def close_popup(self):
        if self.popup_close.is_visible(timeout=2000):
            self.popup_close.click()

    def click_btn_login(self):
        self.btn_login.click()

    def add_product_to_cart(self, index):
        with allure.step(f"Добавление {index} товара в корзину"):
            self.btn_add_to_cart.nth(index).click()
        product = (self.product_name.nth(index)).inner_text()
        print(f'Товар "{product}" добавлен в корзину')

    def check_added_to_cart(self, index):
        with allure.step("Проверка добавленного товара"):
            expect(self.added_to_cart.nth(index)).to_be_visible()

    def go_to_cart_in_header(self):
        self.cart_in_header.click()

    def go_to_cart_page(self):
        with allure.step("Переход на страницу корзины"):
            self.added_to_cart.click()

    def open_cart_from_menu(self):
        self.home_btn.hover()
        self.cart_in_menu.click()