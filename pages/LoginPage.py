import allure

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
    GO_TO_RECOVERY = (By.XPATH, '//*[@name="st.go_to_recovery"]')


class LoginPageHelper(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    def check_page(self):
        with allure.step('Проверяем элементы на странице'):
            self.attach_screenshot()
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

    @allure.step('Нажимаем на кнопку "Войти"')
    def click_login(self):
        self.find_element(LoginPageLocators.LOGIN_BUTTON).click()

    @allure.step('Получаем текст ошибки')
    def get_error_text(self):
        self.attach_screenshot()
        return self.find_element(LoginPageLocators.FILL_LOGIN_AND_EMPTY_PASSWORD_ERROR_TEXT).text

    @allure.step('Вводим логин')
    def input_login(self, login):
        self.find_element(LoginPageLocators.LOGIN_FIELD).send_keys(login)
        self.attach_screenshot()

    @allure.step('Вводим пароль')
    def input_password(self, password):
        self.find_element(LoginPageLocators.PASSWORD_FIELD).send_keys(password)
        self.attach_screenshot()

    @allure.step('Нажимаем на кнопку "Не получается войти"')
    def click_can_not_enter(self):
        self.find_element(LoginPageLocators.LINK_RESTORE).click()

    @allure.step('Переходим к восстановлению')
    def go_to_recovery(self, password):
        for i in range(3):
            with allure.step(f'Вводим неверный пароль {i + 1} раз'):
                self.input_password(password)
                self.click_login()
                self.attach_screenshot()
        self.find_element(LoginPageLocators.GO_TO_RECOVERY).click()

    @allure.step('Переходим к регистрации')
    def click_registration(self):
        self.attach_screenshot()
        self.find_element(LoginPageLocators.REGISTRATION_BUTTON).click()
