import allure

from config.base import BASE_URL
from pages.category_page import CategoryPage


@allure.epic("Каталог и поиск товаров (Catalog)")
@allure.parent_suite("Каталог и поиск товаров (Catalog)")
@allure.feature("Переход на страницу категорий и товаров")
@allure.suite("Переход на страницу категорий и товаров")
class TestCheck:

    @allure.story("Отображение категорий в меню")
    @allure.title("TC_CAT_001 Отображение категорий в меню")
    def test_cat_001(self, page):
        category_page = CategoryPage(page)
        with allure.step("Открыть сайт"):
            category_page.open_page(BASE_URL)
        assert category_page.len_category() == 7, \
            "Количество категорий меньше 7"