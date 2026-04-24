from config.base import BASE_URL
from config.users import USERS_PASSWORD, REGION_ID, COUNTRY_ID
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
        self.field_loginname = self.page.locator("#AccountFrm_loginname")
        self.field_password = self.page.locator("#AccountFrm_password")
        self.field_password_confirm = self.page.locator("#AccountFrm_confirm")
        self.btn_continue = self.page.get_by_role("button", name="Continue")
        self.privacy_policy = self.page.locator("#AccountFrm_agree")


    def fill_first_name(self, fake_data):
        self.field_first_name.fill(fake_data.name())

    def fill_last_name(self, fake_data):
        self.field_last_name.fill(fake_data.last_name())

    def fill_email(self, fake_data):
        self.field_email.fill(fake_data.email())

    def fill_address(self, fake_data):
        self.field_address.fill(fake_data.address())

    def fill_city(self, fake_data):
        self.field_city.fill(fake_data.city())

    def choice_region(self):
        self.field_region.select_option(REGION_ID)

    def choice_country(self):
        self.field_country.select_option(COUNTRY_ID)

    def fill_zipcode(self,fake_data):
        self.field_zipcode.fill(fake_data.postcode())

    def fill_loginname(self, fake_data):
        login = fake_data.user_name()
        self.field_loginname.fill(login)
        return login

    def get_login_value(self):
        return self.field_loginname.input_value()


    def fill_password(self):
        self.field_password.fill(USERS_PASSWORD)

    def fill_password_confirm(self):
        self.field_password_confirm.fill(USERS_PASSWORD)

    def click_continue(self):
        self.btn_continue.click()

    def check_privacy_policy(self):
        self.privacy_policy.check()
