from pages.base_page import BasePage


class CategoryPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.category = self.page.locator(".subcategories")

    def len_category(self):
        return len(self.category)