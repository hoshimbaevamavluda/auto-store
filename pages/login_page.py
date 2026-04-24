from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.continue_to_signup_btn = self.page.get_by_text("Continue")
        self.field_login_name = self.page.locator("#loginFrm_loginname")
        self.field_password = self.page.locator("#loginFrm_password")
        self.btn_login = self.page.get_by_role("button", name="Login")

    def click_btn_continue_to_signup(self):
        self.continue_to_signup_btn.click()

    def fill_login_name(self, login_name):
        self.field_login_name.fill(login_name)

    def fill_password(self, password):
        self.field_password.fill(password)

    def click_login_btn(self):
        self.btn_login.click()
