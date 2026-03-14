from time import sleep

from tests.base_test import BaseTest

class RegistrationTest(BaseTest):
    def setUp(self):
        super().setUp()
        self.authentication_page = self.home_page.click_sign_in()
        self.authentication_page.enter_create_account_email("jask@gmail.com")
    def testNoSurname(self):
        pass