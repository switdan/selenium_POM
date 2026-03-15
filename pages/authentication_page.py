from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from pages.create_account_page import CreateAccountPage


class Locators:
    """
    Authentication Page elements locators
    """
    CREATE_ACCOUNT_EMAIL = (By.ID, "email_create")
    CREATE_ACCOUNT_BTN = (By.ID, "SubmitCreate")


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

    def click_create_account_btn(self):
        """
        Click Create Account button
        :return: CreateAccountPage Object
        """
        self.driver.find_element(*Locators.CREATE_ACCOUNT_BTN).click()
        return CreateAccountPage(self.driver)

    def _verify_page(self):
        """
        Verify that the correct page shown
        """
        WebDriverWait(self.driver, timeout=10).until(EC.title_is("Login - PrestaShop"))