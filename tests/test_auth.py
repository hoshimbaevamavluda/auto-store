import allure
import pytest

from config.base import LOGIN_URL, SUCCESS_URL, ACCOUNT_INFO_URL, E_MSG_LOGIN_PASSWORD
from config.users import USER_NAME, USERS_PASSWORD
from data.data_generator import generate_user
from pages.login_page import LoginPage
from pages.register_page import RegisterPage


user = generate_user()

@allure.epic("Регистрация и Авторизация")
@allure.parent_suite("Регистрация и Авторизация")
@allure.feature("Логин по имени и паролю")
@allure.suite("Логин по имени и паролю")
class TestCheck:

    @allure.story("Успешная регистрация")
    @allure.sub_suite("Успешная регистрация")
    @allure.title("TC_AUTH_001 Успешная регистрация нового пользователя")
    def test_auth_001(self, page):
        """
        :param page:
        :return:
        """

        login_page = LoginPage(page)
        login_page.open_page(LOGIN_URL)
        login_page.click_btn_continue_to_signup()

        register_page = RegisterPage(page)
        register_page.fill_first_name(user["name"])
        register_page.fill_last_name(user["last_name"])
        register_page.fill_email(user["email"])
        register_page.fill_address(user["address"])
        register_page.fill_city(user["city"])
        register_page.choice_country()
        register_page.choice_region()
        register_page.fill_zipcode()
        login = user["login_name"]
        register_page.fill_login_name(login)
        print(login) #для проверки
        assert register_page.get_login_value() == login
        register_page.fill_password(USERS_PASSWORD)
        register_page.fill_password_confirm(USERS_PASSWORD)
        register_page.check_privacy_policy()
        register_page.click_continue()
        register_page.expect_to_have_url(SUCCESS_URL)


    @allure.story("Успешная авторизация")
    @allure.sub_suite("Успешная авторизация")
    @allure.title("TC_AUTH_002 Вход с валидными данными")
    def test_auth_002(self, page):

        """
        :param page:
        :return:
        """

        login_page = LoginPage(page)
        login_page.open_page(LOGIN_URL)
        login_page.fill_login_name(USER_NAME)
        login_page.fill_password(USERS_PASSWORD)
        login_page.click_login_btn()
        login_page.expect_to_have_url(ACCOUNT_INFO_URL)

    @allure.story("Негативные тесты")
    @allure.title("TC_AUTH_003-004 Вход с неверными данными")
    @pytest.mark.flaky
    @pytest.mark.parametrize(
        "login_name, password, error_msg",
        [(USER_NAME, "wrong_pass", E_MSG_LOGIN_PASSWORD),
         ("wrong_email", USERS_PASSWORD, E_MSG_LOGIN_PASSWORD),
        ]
    )
    def test_auth_003_004(self, page, login_name, password, error_msg):
        """
        Тесты Авторизации:
        003 Вход с неверным паролем
        004 Вход с несуществующим логином

        :param page:
        :param login_name:
        :param password:
        :param error_msg:
        :return:
        """

        login_page = LoginPage(page)
        login_page.open_page(LOGIN_URL)
        login_page.fill_login_name(login_name)
        login_page.fill_password(password)
        login_page.click_login_btn()
        login_page.expect_to_have_error_messeg(error_msg)