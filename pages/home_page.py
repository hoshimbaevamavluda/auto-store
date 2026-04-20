from pages.base_page import BasePage


class HomePage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.btn_login = self.page.get_by_text("Login or register")

    def click_btn_login(self):
        self.click(self.btn_login)

