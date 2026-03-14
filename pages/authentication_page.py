from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class Locators:
    """
    Authentication Page elements locators
    """
    CREATE_ACCOUNT_EMAIL = (By.ID, "email_create")


class AuthenticationPage(BasePage):
    """
    Authentication Page Object
    """
    def enter_create_account_email(self, email):
        """
        Type the email for new user registration
        :param email:
        :return:
        """
        self.driver.find_element(*Locators.CREATE_ACCOUNT_EMAIL).send_keys(email)