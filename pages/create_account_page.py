from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pages.base_page import BasePage
from utils.custom_types import Gender

class Locators:
    """
    Create Account Page elements locators
    """
    FIRST_NAME = (By.ID, "customer_firstname")
    LAST_NAME = (By.ID, "customer_lastname")
    MAIL = (By.ID, "email")
    PASSWORD = (By. ID, "passwd")
    TITLE_GENDER_MALE = (By.ID, "id_gender1")
    TITLE_GENDER_FEMALE = (By.ID, "id_gender2")
    DAYS_OF_BIRTH = (By.ID, "days")
    MONTH_OF_BIRTH = (By.ID, "months")
    YEAR_OF_BIRTH = (By.ID, "years")

class CreateAccountPage(BasePage):
    """
    Create Account Page Objects
    """
    def choose_gender(self, gender):
        """
        Choose a gender
        """
        if gender == Gender.MALE:
            self.driver.find_element(*Locators.TITLE_GENDER_MALE).click()
        elif gender == Gender.FEMALE:
            self.driver.find_element(*Locators.TITLE_GENDER_FEMALE).click()

    def enter_first_name(self, first_name):
        self.driver.find_element(*Locators.FIRST_NAME).send_keys(first_name)

    def enter_last_name(self, last_name):
        self.driver.find_element(*Locators.LAST_NAME).send_keys(last_name)

    def get_entered_email(self):
        return self.driver.find_element(*Locators.MAIL).get_attribute("value")

    def password(self, password):
        self.driver.find_element(*Locators.PASSWORD).send_keys(password)

    def choose_day_of_birth(self, day_of_birth):
        Select(self.driver.find_element(*Locators.DAYS_OF_BIRTH)).select_by_value(str(day_of_birth))

    def choose_month_of_birth(self, month_of_birth):
        Select(self.driver.find_element(*Locators.MONTH_OF_BIRTH)).select_by_value(str(month_of_birth))

    def choose_year_of_birth(self, year_of_birth):
        Select(self.driver.find_element(*Locators.YEAR_OF_BIRTH)).select_by_value(str(year_of_birth))

    def _verify_page(self):
        # TODO: Improve this!
        sleep(3)
