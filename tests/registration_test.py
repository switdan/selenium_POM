from time import sleep

from tests.base_test import BaseTest

class RegistrationTest(BaseTest):
    def setUp(self):
        super().setUp()
        self.authentication_page = self.home_page.click_sign_in()
        self.authentication_page.enter_create_account_email("jask@gmail.com")
        self.create_account_page = self.authentication_page.click_create_account_btn()
    def testNoSurname(self):
        self.create_account_page.enter_first_name("Marcin")