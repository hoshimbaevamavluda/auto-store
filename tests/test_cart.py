import allure

from config.base import BASE_URL
from pages.home_page import HomePage


@allure.epic("Корзина (Cart)")
@allure.suite("Добавление в корзину")
class TestCheck:

    @allure.story("Добавление товара")
    @allure.sub_suite("Добавление одного товара")
    @allure.title("TC_CART_001 Добавление одного товара")
    def test_cart_001(self, page):
        home_page = HomePage(page)
        home_page.open_page(BASE_URL)

        home_page.add_to_cart()
        home_page.check_added_to_cart()
