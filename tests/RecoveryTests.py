from core.BaseTest import browser
from pages.BasePage import BasePage
from pages.RecoveryPage import RecoveryPageHelper
from pages.LoginPage import LoginPageHelper
from LoginTests import BASE_URL
from pages.RecoveryByEmailPage import RecoveryPageByEmailHelper
from pages.RecoveryByPhonePage import RecoveryPageByPhoneHelper

EMPTY_PHONE_ERROR_TEXT = 'Неправильный номер телефона.'
EMPTY_EMAIL_ERROR_TEXT = 'Неправильный формат почты'


def test_empty_phone_get_code(browser):
    BasePage(browser).get_url(BASE_URL)
    login_page = LoginPageHelper(browser)
    login_page.click_can_not_enter()
    recovery_page = RecoveryPageHelper(browser)
    recovery_page.click_phone()
    recovery_page_by_phone = RecoveryPageByPhoneHelper(browser)
    recovery_page_by_phone.click_get_code()
    assert recovery_page_by_phone.get_error_text_empty_phone() == EMPTY_PHONE_ERROR_TEXT


def test_empty_email_get_code(browser):
    BasePage(browser).get_url(BASE_URL)
    login_page = LoginPageHelper(browser)
    login_page.click_can_not_enter()
    recovery_page = RecoveryPageHelper(browser)
    recovery_page.click_email()
    recovery_page_by_email = RecoveryPageByEmailHelper(browser)
    recovery_page_by_email.click_get_code()
    assert recovery_page_by_email.get_error_text_empty_email() == EMPTY_EMAIL_ERROR_TEXT
