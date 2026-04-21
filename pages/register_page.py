from config.users import USER_NAME, USERS_PASSWORD, EMAIL_ADDRESS
from pages.base_page import BasePage


class RegisterPage(BasePage):
    FIRST_NAME = "admin"
    ADDRESS = "admin Address"
    CITY = "city"
    ZIPCODE = "zipcode"


    def __init__(self, page):
        super().__init__(page)
        self.field_first_name = self.page.locator("AccountFrm_firstname")
        self.field_last_name = self.page.locator("AccountFrm_lastname")
        self.field_email = self.page.locator("AccountFrm_email")
        self.field_address = self.page.locator("AccountFrm_address_1")
        self.field_city = self.page.locator("AccountFrm_city")
        self.field_region = self.page.locator("AccountFrm_zone_id")
        self.field_zipcode = self.page.locator("AccountFrm_postcode")
        self.field_country = self.page.locator("AccountFrm_country_id")
        self.field_loginname = self.page.locator("AccountFrm_loginname")
        self.field_password = self.page.locator("AccountFrm_password")
        self.field_password_confirm = self.page.locator("AccountFrm_confirm")

    def fill_first_name(self):
        self.field_first_name.fill(self.FIRST_NAME)

    def fill_last_name(self):
        self.field_last_name.fill(self.FIRST_NAME)

    def fill_email(self):
        self.field_email.fill(EMAIL_ADDRESS)

    def fill_address(self):
        self.field_address.fill(self.ADDRESS)

    def fill_city(self):
        self.field_city.fill(self.CITY)

    def click_region(self):
        self.field_region.click()

    def chose_region(self):
        self.field_region.hover()

