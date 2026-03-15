import unittest
from test_data.registration_data_generator import RegistrationDataGenerator
from tests.base_test import BaseTest

class RegistrationTest(BaseTest):
    def setUp(self):
        super().setUp()
        self.data = RegistrationDataGenerator()
        self.authentication_page = self.home_page.click_sign_in()
        self.authentication_page.enter_create_account_email(self.data.EMAIL)
        self.create_account_page = self.authentication_page.click_create_account_btn()


    def testNoLastName(self):
        self.create_account_page.choose_gender(self.data.GENDER)
        self.create_account_page.enter_first_name(self.data.FIRST_NAME)
        self.create_account_page.password(self.data.PASSWORD)
        self.create_account_page.choose_day_of_birth(self.data.DAY)
        self.create_account_page.choose_month_of_birth(self.data.MONTH)
        self.create_account_page.choose_year_of_birth(self.data.YEAR)
        self.create_account_page.click_register()
        assert self.create_account_page.get_red_banner_message() == """There is 1 error\nlastname is required."""

    # @unittest.skip("Temporary skipping")
    def testRegistration(self):
        self.create_account_page.choose_gender(self.data.GENDER)
        self.create_account_page.enter_first_name(self.data.FIRST_NAME)
        self.create_account_page.enter_last_name(self.data.LAST_NAME)
        assert self.create_account_page.get_entered_email() == self.data.EMAIL, \
        (f"Email is incorrect. There is {self.create_account_page.get_entered_email()}, "
         f"but should be {self.data.EMAIL}")
        self.create_account_page.password(self.data.PASSWORD)
        self.create_account_page.choose_day_of_birth(self.data.DAY)
        self.create_account_page.choose_month_of_birth(self.data.MONTH)
        self.create_account_page.choose_year_of_birth(self.data.YEAR)
        self.create_account_page.click_register()
