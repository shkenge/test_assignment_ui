from .base_page import BasePage
from .locators import LoginPageLocators
from .data_for_tests import LogInPageData
import logging


class LoginPage(BasePage):

    def login(self, valid_email, random_valid_password):
        self.input_email_login(valid_email)
        self.input_password_login(random_valid_password)
        self.click_button_login()

    def input_email_login(self, valid_email):
        logging.info(f"Input email {valid_email}")
        self.browser.find_element(*LoginPageLocators.login_email_input_field).send_keys(valid_email)

    def input_password_login(self, random_valid_password):
        logging.info(f"Input password {random_valid_password}")
        self.browser.find_element(*LoginPageLocators.login_password_input_field).send_keys(random_valid_password)

    def click_button_login(self):
        logging.info("Click button login")
        self.browser.find_element(*LoginPageLocators.login_button).click()

    def should_not_log_in(self):
        assert self.browser.find_element(*LoginPageLocators.notification).text == LogInPageData.error_notification, \
            "Wrong error message when login"
