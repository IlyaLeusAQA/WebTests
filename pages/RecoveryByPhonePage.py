import allure
from pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class RecoveryPageByPhoneLocators:
    GET_CODE_BUTTON = (By.XPATH, '//*[@data-l="t,submit"]')
    EMPTY_PHONE_ERROR_TEXT = (By.XPATH, '//*[@class="input-e js-ph-vl-hint"]')
    ENTER_PHONE_TITLE = (By.XPATH, '//*[@for="field_phone"]')
    FIELD_NUMBER_PHONE = (By.XPATH, '//*[@id="field_phone"]')
    COUNTRY_REGION = (By.XPATH, '//*[@id="country"]')


class RecoveryPageByPhoneHelper(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    def check_page(self):
        with allure.step('Проверяем элементы на странице'):
            self.attach_screenshot()
            self.find_element(RecoveryPageByPhoneLocators.GET_CODE_BUTTON)
            self.find_element(RecoveryPageByPhoneLocators.ENTER_PHONE_TITLE)
            self.find_element(RecoveryPageByPhoneLocators.FIELD_NUMBER_PHONE)
            self.find_element(RecoveryPageByPhoneLocators.COUNTRY_REGION)

    @allure.step('Нажимаем на кнопку "Получить код"')
    def click_get_code(self):
        self.find_element(RecoveryPageByPhoneLocators.GET_CODE_BUTTON).click()

    @allure.step('Получаем текст ошибки при пустом поле телефон')
    def get_error_text_empty_phone(self):
        self.attach_screenshot()
        return self.find_element(RecoveryPageByPhoneLocators.EMPTY_PHONE_ERROR_TEXT).text
