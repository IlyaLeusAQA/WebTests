import allure
from pages.BasePage import BasePageHelper
from selenium.webdriver.common.by import By


class VkEcosystemLocators:
    TITLE_LABEL = (By.XPATH, '//h1[@class="title-h2"]')


class VkEcosystemHelper(BasePageHelper):

    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    def check_page(self):
        with allure.step('Проверяем элементы на странице'):
            self.attach_screenshot()
        self.find_element(VkEcosystemLocators.TITLE_LABEL)
