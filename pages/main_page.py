from .base_page import BasePage
from .locators import MainPageLocators
import logging


class MainPage(BasePage):

    def click_button_navigator_bar(self, click_button):
        logging.info(f"Click button {click_button} from navigator bar")
        self.browser.find_element(*click_button).click()

    def get_navigator_bar(self):
        logging.info("Get navigator bar from main page")
        return self.browser.find_element(*MainPageLocators.nav_bar_menu)

    def should_be_text_main_page(self):
        main_page_check = self.browser.find_element(*MainPageLocators.main_page_text).text
        assert main_page_check == "Test home page", "Text in main page incorrect"

    def should_be_open_page(self, get_url, check_url):
        assert get_url == check_url, "URL page incorrect"

    def should_be_navigator_bar(self, navigator_bar):
        assert navigator_bar.is_displayed(), "Navigator bar is not displayed on the page"
