from faker import Faker
from utils.custom_types import Gender
import random

class RegistrationDataGenerator:
    def __init__(self):
        self.GENDER = random.choice([Gender.MALE, Gender.FEMALE])
        self.fake = Faker("pl_PL")
        if self.GENDER == Gender.MALE:
            self.FIRST_NAME = self.fake.first_name_male()
            self.SECOND_NAME = self.fake.last_name_male()
        elif self.GENDER == Gender.FEMALE:
            self.FIRST_NAME = self.fake.first_name_female()
            self.SECOND_NAME = self.fake.last_name_female()
        self.EMAIL = self.fake.email()
        self.PASSWORD = self.fake.password()
        self.DAY = self.fake.day_of_month()
        self.MONTH = self.fake.month()
        self.YEAR = self.fake.year()
