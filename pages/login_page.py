from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.continue_to_signup_btn = self.page.get_by_text("Continue")

    def click_btn_continue_to_signup(self):
        self.click(self.continue_to_signup_btn)

