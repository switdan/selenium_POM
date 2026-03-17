import unittest

import test_data.registration_data
from test_data.registration_data import RegistrationDataGenerator
from tests.base_test import BaseTest
from ddt import ddt, data, unpack

@ddt
class RegistrationTest(BaseTest):
    def setUp(self):
        super().setUp()
        self.data = RegistrationDataGenerator()
        self.authentication_page = self.home_page.click_sign_in()
        self.authentication_page.enter_create_account_email(self.data.EMAIL)
        self.create_account_page = self.authentication_page.click_create_account_btn()

    @data(*test_data.registration_data.get_csv_data("test_data/registration.csv"))
    @unpack
    def testNoLastName(self, gender, firstname, lastname, email, password, day, month, year):
        self.create_account_page.choose_gender(self.data.GENDER)
        self.create_account_page.enter_first_name(firstname)
        self.create_account_page.password(password)
        self.create_account_page.choose_day_of_birth(day)
        self.create_account_page.choose_month_of_birth(month)
        self.create_account_page.choose_year_of_birth(year)
        self.create_account_page.click_register()
        assert self.create_account_page.get_red_banner_message_if_password_missing() == """There is 1 error\nlastname is required."""

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
