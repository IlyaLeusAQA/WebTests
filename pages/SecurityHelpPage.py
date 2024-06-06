from pages.BasePage import BasePage
from selenium.webdriver.common.by import By
import allure


class SecurityHelpPageLocators:
    TITLE = (By.XPATH, '//span[text()= "Безопасность"]')
    HELP_GET_VIDEO_OK = (By.XPATH, '//*[text()= "Что делать, если не воспроизводится видео в «Одноклассниках»?"]')
    DOWNLOAD_VIDEO_IN_OK_WITH_YOUTUBE = (By.XPATH, '//*[text()= "Как загрузить видео в Одноклассниках с Ютуба?"]')
    BUTTON_YES = (By.XPATH, '//span[text()= "Да"]')
    THANKS_FOR_ANSWER = (By.XPATH, '//div[text()= "Спасибо за ответ!"]')
    WAS_THIS_ANSWER_HELPFUL = (By.XPATH, '//span[text()= "Был ли этот ответ полезным?"]')


class SecurityHelpPageHelper(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    def check_page(self):
        with allure.step('Проверяем корректность загрузки страницы'):
            self.attach_screenshot()
        self.find_element(SecurityHelpPageLocators.TITLE)
        self.find_element(SecurityHelpPageLocators.HELP_GET_VIDEO_OK)

    def click_cant_playing_video_in_ok(self):
        self.find_element(SecurityHelpPageLocators.HELP_GET_VIDEO_OK).click()

    def click_yes(self):
        self.find_element(SecurityHelpPageLocators.BUTTON_YES).click()

    def check_congrats_for_answer(self):
        with allure.step('Проверяем корректность ответа'):
            self.attach_screenshot()
        self.find_element(SecurityHelpPageLocators.THANKS_FOR_ANSWER)
