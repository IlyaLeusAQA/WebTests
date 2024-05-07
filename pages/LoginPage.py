from pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_FIELD = (By.ID, 'field_email')
    PASSWORD_FIELD = (By.ID, 'field_password')
    LOGIN_BUTTON = (By.XPATH, '//*[@data-l="t,sign_in"]')
    LOGIN_QR_BUTTON = (By.XPATH, '//*[@data-l="t,get_qr"]')
    BUTTON_ENTER = (By.XPATH, '//*[@data-l="t,login_tab"]')
    BUTTON_QR = (By.XPATH, '//*[@data-l="t,qr_tab"]')
    LINK_RESTORE = (By.XPATH, '//*[@data-l="t,restore"]')
    REGISTRATION_BUTTON = (By.XPATH, '//*[@class="button-pro __sec mb-3x __wide"]')
    LOGIN_BUTTON_VK_ID = (By.XPATH, '//*[@data-l="t,vkc"]')
    LOGIN_WITH_EMAIL = (By.XPATH, '//*[@data-l="t,mailru"]')
    LOGIN_INTO_YANDEX = (By.XPATH, '//*[@data-l="t,yandex"]')
    OTHER_VARIANT_LOGIN = (By.XPATH, '//*[@data-l="t,other"]')
    FILL_LOGIN_AND_EMPTY_PASSWORD_ERROR_TEXT = (By.XPATH, '//*[@class="input-e login_error"]')


class LoginPageHelper(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    def check_page(self):
        self.find_element(LoginPageLocators.LOGIN_FIELD)
        self.find_element(LoginPageLocators.PASSWORD_FIELD)
        self.find_element(LoginPageLocators.LOGIN_BUTTON)
        self.find_element(LoginPageLocators.LOGIN_QR_BUTTON)
        self.find_element(LoginPageLocators.BUTTON_ENTER)
        self.find_element(LoginPageLocators.BUTTON_QR)
        self.find_element(LoginPageLocators.LINK_RESTORE)
        self.find_element(LoginPageLocators.REGISTRATION_BUTTON)
        self.find_element(LoginPageLocators.LOGIN_BUTTON_VK_ID)
        self.find_element(LoginPageLocators.LOGIN_WITH_EMAIL)
        self.find_element(LoginPageLocators.LOGIN_INTO_YANDEX)
        self.find_element(LoginPageLocators.OTHER_VARIANT_LOGIN)

    def click_login(self):
        self.find_element(LoginPageLocators.LOGIN_BUTTON).click()

    def get_error_text(self):
        return self.find_element(LoginPageLocators.FILL_LOGIN_AND_EMPTY_PASSWORD_ERROR_TEXT).text

    def input_login(self, login):
        self.find_element(LoginPageLocators.LOGIN_FIELD).send_keys(login)

    def input_password(self, password):
        self.find_element(LoginPageLocators.PASSWORD_FIELD).send_keys(password)
