from config.base import LOGIN_URL, SUCCESS_URL, ACCOUNT_INFO_URL
from config.users import USER_NAME, USERS_PASSWORD
from pages.login_page import LoginPage
from pages.register_page import RegisterPage
from faker import Faker


class TestCheck:

    def test_auth_001(self, page):
        """
        Успешная регистрация нового пользователя
        """

        login_page = LoginPage(page)
        login_page.open_page(LOGIN_URL)
        login_page.click_btn_continue_to_signup()

        register_page = RegisterPage(page)
        register_page.fill_first_name(Faker().name())
        register_page.fill_last_name(Faker().last_name())
        register_page.fill_email(Faker().unique.email())
        register_page.fill_address(Faker().address())
        register_page.fill_city(Faker().city())
        register_page.choice_country()
        register_page.choice_region()
        register_page.fill_zipcode()
        login = register_page.fill_login_name()
        print(login) #для проверки
        assert register_page.get_login_value() == login
        register_page.fill_password()
        register_page.fill_password_confirm()
        register_page.check_privacy_policy()
        register_page.click_continue()
        register_page.expect_to_have_url(SUCCESS_URL)

    def test_auth_002(self, page):
        """
        Вход с валидными данными
        """

        login_page = LoginPage(page)
        login_page.open_page(LOGIN_URL)
        login_page.fill_login_name(USER_NAME)
        login_page.fill_password(USERS_PASSWORD)
        login_page.click_login_btn()
        login_page.expect_to_have_url(ACCOUNT_INFO_URL)

    def test_auth_003(self, page):
        """
        Вход с неверным паролем
        """

        login_page = LoginPage(page)
        login_page.open_page(LOGIN_URL)
        login_page.fill_login_name(USER_NAME)
        login_page.fill_password("wrong_pass")
        login_page.click_login_btn()
        error_text = "Error: Incorrect login or password provided."
        login_page.expect_to_have_error_messeg(error_text)

    def test_auth_004(self, page):
        """
        Вход с несуществующим email
        """

        login_page = LoginPage(page)
        login_page.open_page(LOGIN_URL)
        login_page.fill_login_name("wrong_email")
        login_page.fill_password(USERS_PASSWORD)
        login_page.click_login_btn()
        error_text = "Error: Incorrect login or password provided."
        login_page.expect_to_have_error_messeg(error_text)