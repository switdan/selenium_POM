from faker import Faker
from utils.custom_types import Gender
import random

class RegistrationDataGenerator:
    def __init__(self):
        self.GENDER = random.choice([Gender.MALE, Gender.FEMALE])
        self.__fake = Faker("pl_PL")
        if self.GENDER == Gender.MALE:
            self.FIRST_NAME = self.__fake.first_name_male()
            self.LAST_NAME = self.__fake.last_name_male()
        elif self.GENDER == Gender.FEMALE:
            self.FIRST_NAME = self.__fake.first_name_female()
            self.LAST_NAME = self.__fake.last_name_female()
        self.EMAIL = self.__fake.email()
        self.PASSWORD = self.__fake.password()
        self.DAY = int(self.__fake.day_of_month())
        self.MONTH = int(self.__fake.month())
        self.YEAR = int(self.__fake.year())

print(RegistrationDataGenerator().MONTH)