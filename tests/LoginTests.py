import allure

from core.BaseTest import browser
from pages.BasePage import BasePage
from pages.LoginPage import LoginPageHelper

BASE_URL = 'https://ok.ru'
EMPTY_LOGIN_ERROR = 'Введите логин'
WRONG_LOGIN = 'error_login'
WRONG_PASSWORD = '12345'
ERROR_TEXT_WITH_EMPTY_PASSWORD = 'Введите пароль'
ERROR_TEXT_WITH_WRONG_PASSWORD_AND_LOGIN = 'Неправильно указан логин и/или пароль'


@allure.suite('Проверка страницы авторизации')
@allure.title('Проверка корректности ошибки при пустом логине и пароле')
def test_empty_login_and_password(browser):
    BasePage(browser).get_url(BASE_URL)
    login_page = LoginPageHelper(browser)
    login_page.click_login()
    with allure.step(f'Проверка, что текст ошибки соответствует: {EMPTY_LOGIN_ERROR}'):
        assert login_page.get_error_text() == EMPTY_LOGIN_ERROR


@allure.suite('Проверка страницы авторизации')
@allure.title('Проверка корректности ошибки при заполненном логине и пустом пароле')
def test_fill_login_and_empty_password(browser):
    BasePage(browser).get_url(BASE_URL)
    login_page = LoginPageHelper(browser)
    login_page.input_login(WRONG_LOGIN)
    login_page.click_login()
    with allure.step(f'Проверка, что текст ошибки соответствует: {ERROR_TEXT_WITH_EMPTY_PASSWORD}'):
        assert login_page.get_error_text() == ERROR_TEXT_WITH_EMPTY_PASSWORD


@allure.suite('Проверка страницы авторизации')
@allure.title('Проверка корректности ошибки при неверном логине и пароле')
def test_wrong_login_and_wrong_password(browser):
    BasePage(browser).get_url(BASE_URL)
    login_page = LoginPageHelper(browser)
    login_page.input_login(WRONG_LOGIN)
    login_page.input_password(WRONG_PASSWORD)
    login_page.click_login()
    with allure.step(f'Проверка, что текст ошибки соответствует: {ERROR_TEXT_WITH_WRONG_PASSWORD_AND_LOGIN}'):
        assert login_page.get_error_text() == ERROR_TEXT_WITH_WRONG_PASSWORD_AND_LOGIN
