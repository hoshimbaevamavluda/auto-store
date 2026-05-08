import allure

from config.base import BASE_URL, TXT_EMPTY_CART, CART_URL
from pages.cart_page import CartPage
from pages.home_page import HomePage


@allure.epic("Корзина (Cart)")
@allure.suite("Добавление в корзину")
class TestCheck:

    @allure.story("Добавление товара")
    @allure.sub_suite("Добавление одного товара")
    @allure.title("TC_CART_001 Добавление одного товара")
    def test_cart_001(self, page):
        home_page = HomePage(page)
        with allure.step("Открытие страницы"):
            home_page.open_page(BASE_URL)
        with allure.step("Добавление товара в корзину"):
            home_page.add_product_to_cart(0)
        with allure.step("Проверка добавленного товара"):
            home_page.check_added_to_cart(0)

    @allure.story("Добавление товара")
    @allure.sub_suite("Добавление нескольких разных товаров")
    @allure.title("TC_CART_002 Добавление нескольких разных товаров")
    def test_cart_002(self, page):
        home_page = HomePage(page)
        home_page.open_page(BASE_URL)
        with allure.step("Открытие страницы"):
            home_page.open_page(BASE_URL)
        for i in range(3):
            with allure.step(f"Добавление {i} товара в корзину"):
                home_page.add_product_to_cart(i)
            with allure.step("Проверка добавленного товара"):
                home_page.check_added_to_cart(i)

    @allure.story("Удаление товара")
    @allure.sub_suite("Удаление товара")
    @allure.title("TC_CART_003 Удаление товара")
    def test_cart_003(self, page):
        home_page = HomePage(page)
        cart_page = CartPage(page)
        with allure.step("Открытие страницы"):
            home_page.open_page(BASE_URL)
        with allure.step("Добавление товара в корзину"):
            home_page.add_product_to_cart(0)
        with allure.step("Переход на страницу корзины"):
            home_page.go_to_cart_page()
        with allure.step("Удаление товара"):
            cart_page.del_item_in_cart()
        cart_page.expect_to_empty_cart(TXT_EMPTY_CART)
        print("Товар успещно удален")

    @allure.story("Обновление количества товара")
    @allure.sub_suite("Обновление количества товара")
    @allure.title("TC_CART_004 Обновление количества товара")
    def test_cart_004(self, page):
        home_page = HomePage(page)
        cart_page = CartPage(page)
        with allure.step("Открытие страницы"):
            home_page.open_page(BASE_URL)
        with allure.step("Добавление товара в корзину"):
            home_page.add_product_to_cart(0)
        with allure.step("Переход на страницу корзины"):
            home_page.go_to_cart_page()
        with allure.step("Обновление количества товара на 3"):
            cart_page.change_quantity("3")

    @allure.story("Пустая корзина: отображение")
    @allure.sub_suite("Пустая корзина: отображение")
    @allure.title("TC_CART_005 Пустая корзина: отображение")
    def test_cart_005(self, page):
        home_page = HomePage(page)
        cart_page = CartPage(page)
        with allure.step("Открытие страницы"):
            home_page.open_page(BASE_URL)
        with allure.step("Переход на страницу корзины"):
            home_page.open_cart_from_menu()
        with allure.step("Проверка пустой корзины по тексту"):
            cart_page.expect_to_empty_cart(TXT_EMPTY_CART)

    @allure.story("Переход в корзину с любой страницы")
    @allure.sub_suite("Переход в корзину с любой страницы")
    @allure.title("TC_CART_006 Переход в корзину с любой страницы")
    def test_cart_006(self, page):
        home_page = HomePage(page)
        with allure.step("Открытие страницы"):
            home_page.open_page(BASE_URL)
        with allure.step("Переход на страницу корзины"):
            home_page.go_to_cart_in_header()
            home_page.expect_to_have_url(CART_URL)
