import allure
from pages.BasePage import BasePageHelper
from selenium.webdriver.common.by import By


class RecoveryPageByEmailLocators:
    GET_CODE_BUTTON = (By.XPATH, '//*[@data-l="t,submit"]')
    EMPTY_EMAIL_ERROR_TEXT = (By.XPATH, '//*[@class="input-e"]')
    EMAIL_TITLE = (By.XPATH, '//*[@class="ext-registration_h"]')
    LABEL_FOR_FIELD_EMAIL = (By.XPATH, '//*[@for="field_email"]')
    FIELD_EMAIL = (By.XPATH, '//*[@id="field_email"]')


class RecoveryPageByEmailHelper(BasePageHelper):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    def check_page(self):
        with allure.step('Проверяем элементы на странице'):
            self.attach_screenshot()
            self.find_element(RecoveryPageByEmailLocators.GET_CODE_BUTTON)
            self.find_element(RecoveryPageByEmailLocators.EMAIL_TITLE)
            self.find_element(RecoveryPageByEmailLocators.LABEL_FOR_FIELD_EMAIL)
            self.find_element(RecoveryPageByEmailLocators.FIELD_EMAIL)

    @allure.step('Нажимаем на кнопку "Получить код"')
    def click_get_code(self):
        self.find_element(RecoveryPageByEmailLocators.GET_CODE_BUTTON).click()

    @allure.step('Получаем текст ошибки при пустом поле почта')
    def get_error_text_empty_email(self):
        self.attach_screenshot()
        return self.find_element(RecoveryPageByEmailLocators.EMPTY_EMAIL_ERROR_TEXT).text
