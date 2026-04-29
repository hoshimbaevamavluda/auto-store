import pytest

from config.base import LOGIN_URL
from pages.login_page import LoginPage


class TestMobileCheck:
    @pytest.mark.parametrize("mobile", ["iPhone 14", "Pixel 5"], indirect=True)
    def test_check_mobile_001(self, mobile):
        login_page = LoginPage(mobile)
        login_page.open_page(LOGIN_URL)
        login_page.click_btn_continue_to_signup()

