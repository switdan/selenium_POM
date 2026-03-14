from time import sleep

from selenium.webdriver.common.by import By

from pages.base_page import BasePage

class Locators:
    """
    Create Account Page elements locators
    """
    FIRST_NAME = (By.ID, "customer_firstname")

class CreateAccountPage(BasePage):
    """
    Create Account Page Objects
    """
    def choose_gender(self, gender):
        pass
    def enter_first_name(self, first_name):
        self.driver.find_element(*Locators.FIRST_NAME).send_keys(first_name)
    def _verify_page(self):
        # TODO: Improve this!
        sleep(3)
