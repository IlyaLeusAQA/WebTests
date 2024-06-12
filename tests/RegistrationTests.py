import allure

from core.BaseTest import browser
from pages.BasePage import BasePageHelper
from pages.LoginPage import LoginPageHelper
from pages.RegistrationPage import RegistrationPageHelper

BASE_URL = 'https://ok.ru'


@allure.suite('Проверка страницы регистрации')
@allure.title('Выбор страны и проверка соответствия кода этой страны')
def test_select_country(browser):
    BasePageHelper(browser).get_url(BASE_URL)
    login_page = LoginPageHelper(browser)
    login_page.click_registration()
    registration_page = RegistrationPageHelper(browser)
    assert registration_page.random_country_select() == registration_page.get_country_code()
    pass
