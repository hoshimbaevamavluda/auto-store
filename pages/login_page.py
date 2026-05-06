from playwright.sync_api import expect

from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.continue_to_signup_btn = self.page.get_by_text("Continue")
        self.field_login_name = self.page.locator("#loginFrm_loginname")
        self.field_password = self.page.locator("#loginFrm_password")
        self.btn_login = self.page.get_by_role("button", name="Login")
        self.error_message = self.page.locator(".alert.alert-error.alert-danger")

    def click_btn_continue_to_signup(self):
        self.continue_to_signup_btn.click()

    def fill_login_name(self, login_name):
        self.field_login_name.fill(login_name)

    def fill_password(self, password):
        self.field_password.fill(password)

    def click_login_btn(self):
        self.btn_login.click()

    def expect_to_have_error_message(self, error_msg):
        expect(self.error_message).to_contain_text(error_msg)
