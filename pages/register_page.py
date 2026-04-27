from faker import Faker

from config.users import USERS_PASSWORD, REGION_ID, COUNTRY_ID, ZIP_CODE
from pages.base_page import BasePage


class RegisterPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.field_first_name = self.page.locator("#AccountFrm_firstname")
        self.field_last_name = self.page.locator("#AccountFrm_lastname")
        self.field_email = self.page.locator("#AccountFrm_email")
        self.field_address = self.page.locator("#AccountFrm_address_1")
        self.field_city = self.page.locator("#AccountFrm_city")
        self.field_region = self.page.locator("#AccountFrm_zone_id")
        self.field_zipcode = self.page.locator("#AccountFrm_postcode")
        self.field_country = self.page.locator("#AccountFrm_country_id")
        self.field_login_name = self.page.locator("#AccountFrm_loginname")
        self.field_password = self.page.locator("#AccountFrm_password")
        self.field_password_confirm = self.page.locator("#AccountFrm_confirm")
        self.btn_continue = self.page.get_by_role("button", name="Continue")
        self.privacy_policy = self.page.locator("#AccountFrm_agree")


    def fill_first_name(self, name):
        self.field_first_name.fill(name)

    def fill_last_name(self, last_name):
        self.field_last_name.fill(last_name)

    def fill_email(self, email):
        self.field_email.fill(email)

    def fill_address(self, address):
        self.field_address.fill(address)

    def fill_city(self, city):
        self.field_city.fill(city)

    def choice_region(self):
        self.field_region.select_option(REGION_ID)

    def choice_country(self):
        self.field_country.select_option(COUNTRY_ID)

    def fill_zipcode(self):
        self.field_zipcode.fill(ZIP_CODE)

    def fill_login_name(self):
        login = Faker().user_name()
        self.field_login_name.fill(login)
        return login

    def get_login_value(self):
        return self.field_login_name.input_value()


    def fill_password(self):
        self.field_password.fill(USERS_PASSWORD)

    def fill_password_confirm(self):
        self.field_password_confirm.fill(USERS_PASSWORD)

    def click_continue(self):
        self.btn_continue.click()

    def check_privacy_policy(self):
        self.privacy_policy.check()
