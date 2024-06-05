import allure

from pages.BasePage import BasePage
from core.BaseTest import browser
from pages.HelpPage import HelpPageLocators, HelpPageHelper
from pages.AdvetisementCabinetHelp import AdvertisementCabinetPageHelper
from pages.SecurityHelpPage import SecurityHelpPageHelper, SecurityHelpPageLocators

BASE_URL = 'https://ok.ru/help'


@allure.suite('Проверка страницы помощи')
@allure.title('Проверка названия страницы "Рекламный кабинет"')
def test_help_for_advetisement(browser):
    BasePage(browser).get_url(BASE_URL)
    HelpPage = HelpPageHelper(browser)
    HelpPage.scrollToItem(HelpPageLocators.ADVERTISEMENT_CABINET)
    AdvertisementCabinetPageHelper(browser)


@allure.suite('Проверка страницы помощи')
@allure.title('Проверка ответа на обратную связь')
def test_help_download_video(browser):
    BasePage(browser).get_url(BASE_URL)
    HelpPage = HelpPageHelper(browser)
    HelpPage.scrollToItem(HelpPageLocators.SECURITY)
    SecurityPage = SecurityHelpPageHelper(browser)
    SecurityPage.click_cant_playing_video_in_ok()
    HelpPage.scrollToItem(SecurityHelpPageLocators.DOWNLOAD_VIDEO_IN_OK_WITH_YOUTUBE)
    HelpPage.scrollToItem(SecurityHelpPageLocators.WAS_THIS_ANSWER_HELPFUL)
    SecurityPage.click_yes()
    SecurityPage.check_congrats_for_answer()
