from faker import Faker
from utils.custom_types import Gender
import random

class RegistrationDataGenerator:
    def __init__(self):
        self.GENDER = random.choice([Gender.MALE, Gender.FEMALE])
        self.fake = Faker("pl_PL")
        if self.GENDER == Gender.MALE:
            self.FIRST_NAME = self.fake.first_name_male()
            self.LAST_NAME = self.fake.last_name_male()
        elif self.GENDER == Gender.FEMALE:
            self.FIRST_NAME = self.fake.first_name_female()
            self.LAST_NAME = self.fake.last_name_female()
        self.EMAIL = self.fake.email()
        self.PASSWORD = self.fake.password()
        self.DAY = int(self.fake.day_of_month())
        self.MONTH = int(self.fake.month())
        self.YEAR = int(self.fake.year())

print(RegistrationDataGenerator().MONTH)