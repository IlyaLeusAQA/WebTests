import allure
from pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class RecoveryPageLocators:
    PHONE_BUTTON = (By.XPATH, '//*[@data-l="t,phone"]')
    EMAIL_BUTTON = (By.XPATH, '//*[@data-l="t,email"]')
    SUPPORT_LINK_BUTTON = (By.XPATH, '//*[@class="support-link_item-text"]')
    RECOVERY_ACCESS = (By.XPATH, '//*[@class="ext-registration_h"]')
    WHAT_REMEMBERS_OF_PROFILE = (By.XPATH, '//*[@class="ext-registration_tx taCenter"]')
    QR_IMAGE = (By.XPATH, '//*[@class="qr_code_image"]')
    USE_OK_FOR_MOBILE = (By.XPATH, '//*[@class="qr_code_info_header"]')
    INSTRUCTION = (By.XPATH, '//*[@class="qr_code_info_instruction"]')
    OUR_AUTHORIZATION_CODE = (By.XPATH, '//*[@class="qr_code_info_digest_info"]')


class RecoveryPageHelper(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    def check_page(self):
        with allure.step('Проверяем элементы на странице'):
            self.attach_screenshot()
            self.find_element(RecoveryPageLocators.PHONE_BUTTON)
            self.find_element(RecoveryPageLocators.EMAIL_BUTTON)
            self.find_element(RecoveryPageLocators.SUPPORT_LINK_BUTTON)
            self.find_element(RecoveryPageLocators.RECOVERY_ACCESS)
            self.find_element(RecoveryPageLocators.WHAT_REMEMBERS_OF_PROFILE)
            self.find_element(RecoveryPageLocators.QR_IMAGE)
            self.find_element(RecoveryPageLocators.USE_OK_FOR_MOBILE)
            self.find_element(RecoveryPageLocators.INSTRUCTION)
            self.find_element(RecoveryPageLocators.OUR_AUTHORIZATION_CODE)

    @allure.step('Нажимаем на кнопку "Телефон"')
    def click_phone(self):
        self.find_element(RecoveryPageLocators.PHONE_BUTTON).click()

    @allure.step('Нажимаем на кнопку "Почта"')
    def click_email(self):
        self.find_element(RecoveryPageLocators.EMAIL_BUTTON).click()

    @allure.step('Нажимаем на кнопку "Обратиться в службу поддержки"')
    def click_support(self):
        self.find_element(RecoveryPageLocators.SUPPORT_LINK_BUTTON).click()
