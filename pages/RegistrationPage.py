from pages.BasePage import BasePageHelper
from selenium.webdriver.common.by import By
import allure
import random


class RegistrationPageLocators:
    PHONE_FIELD = (By.XPATH, '//*[@data-l="t,phone"]')
    COUNTRY_LIST = (By.XPATH, '//div[@data-l="t,country"]')
    COUNTRY_ITEM = (By.XPATH, '//div[@class="country-select_code"]')
    SUBMIT_BUTTON = (By.XPATH, '//input[@data-l="t,submit"]')
    SUPPORT_BUTTON = (By.XPATH, '//*[@data-l="t,support"]')


class RegistrationPageHelper(BasePageHelper):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    def check_page(self):
        with allure.step('Проверяем элементы на странице'):
            self.attach_screenshot()
            self.find_element(RegistrationPageLocators.PHONE_FIELD)
            self.find_element(RegistrationPageLocators.COUNTRY_LIST)
            self.find_element(RegistrationPageLocators.SUPPORT_BUTTON)
            self.find_element(RegistrationPageLocators.SUBMIT_BUTTON)

    def random_country_select(self):
        with allure.step('Проверяем выбор страны и код'):
            random_number = random.randint(0, 212)
            self.find_element(RegistrationPageLocators.COUNTRY_LIST).click()
            country_items = self.find_elements(RegistrationPageLocators.COUNTRY_ITEM)
            country_code = country_items[random_number].get_attribute("text")
            country_items[random_number].click()
            self.attach_screenshot()
            return country_code

    def get_country_code(self):
        country_code_in_phone_field = self.find_element(RegistrationPageLocators.PHONE_FIELD).get_attribute("value")
        return country_code_in_phone_field
