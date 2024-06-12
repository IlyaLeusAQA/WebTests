import allure

from core.BaseTest import browser
from pages.BasePage import BasePageHelper
from pages.LoginPage import LoginPageHelper
from pages.VkEcosystemPage import VkEcosystemHelper

BASE_URL = 'https://ok.ru'


@allure.suite('Проверка тулбара')
@allure.title('Переход к проектам экосистемы VK')
def test_open_vk_ecosystem(browser):
    BasePage = BasePageHelper(browser)
    BasePage.get_url(BASE_URL)
    BasePage.check_page()
    login_page = LoginPageHelper(browser)
    current_window_id = login_page.get_windows_id(0)
    login_page.click_eco_system()
    login_page.click_more_button()
    new_window_id = login_page.get_windows_id(1)
    login_page.change_window(new_window_id)
    VkEcosystem = VkEcosystemHelper(browser)
    VkEcosystem.change_window(current_window_id)
    LoginPageHelper(browser)
