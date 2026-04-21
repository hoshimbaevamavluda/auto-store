from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.register_page import RegisterPage


class TestCheck:

    def test_auth_001(self, page):
        hm_page = HomePage(page)
        hm_page.open_page()
        hm_page.click_btn_login()

        login_page = LoginPage(page)
        login_page.click_btn_continue_to_signup()

        register_page = RegisterPage(page)
        register_page.fill_first_name()
        register_page.fill_last_name()
        register_page.fill_email()
        register_page.fill_address()
        register_page.fill_city()
        register_page.click_region()
        register_page.chose_region()










