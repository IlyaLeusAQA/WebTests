from pages.BasePage import BasePage
from selenium.webdriver.common.by import By

class LoginPageLocators:
    LOGIN_FIELD = (By.ID, 'field_email')
    PASSWORD_FIELD = (By.ID, 'field_password')
    LOGIN_BUTTON = (By.XPATH, '//*[@data-l="t,sign_in"]')
    LOGIN_QR_BUTTON = (By.XPATH, '//*[@data-l="t,get_qr"]')
    BUTTON_ENTER = (By.XPATH, '//*[@data-l="t,login_tab"]')
    BUTTON_QR = (By.XPATH, '//*[@data-l="t,qr_tab"]')
    LINK_RESTORE = (By.XPATH,'//*[@data-l="t,restore"]')
    REGISTRATION_BUTTON = (By.XPATH, '//*[@data-l="t,register"]')
    LOGIN_BUTTON_VK_ID = (By.XPATH, '//*[@data-l="t,vkc"]')
    LOGIN_WITH_EMAIL = (By.XPATH, '//*[@data-l="t,mailru"]')
    LOGIN_INTO_YANDEX = (By.XPATH, '//*[@data-l="t,yandex"]')
    OTHER_VARIANT_LOGIN = (By.XPATH, '//*[@data-l="t,other"]')

class LoginPageHelper(BasePage):
    pass