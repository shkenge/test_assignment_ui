from .base_page import BasePage
from .locators import SignInPageLocators
from .locators import LoginPageLocators
import logging


class SignUpPage(BasePage):

    def sign_up(self, input_email, input_name, input_random_password):
        self.input_email_sign_up(input_email)
        self.input_name_sign_up(input_name)
        self.input_password_sign_up(input_random_password)
        self.click_button_sign_up()

    def input_email_sign_up(self, input_email):
        logging.info(f"Input email {input_email}")
        self.browser.find_element(*SignInPageLocators.sign_in_email_input_field).send_keys(input_email)

    def input_name_sign_up(self, input_name):
        logging.info(f"Input name {input_name}")
        self.browser.find_element(*SignInPageLocators.sign_in_email_input_name).send_keys(input_name)

    def input_password_sign_up(self, input_random_password):
        logging.info(f"Input password {input_random_password}")
        self.browser.find_element(*SignInPageLocators.sign_in_password_input_field).send_keys(input_random_password)

    def click_button_sign_up(self):
        logging.info("Click button Sign Up")
        self.browser.find_element(*SignInPageLocators.sign_in_button).click()

    def should_be_open_login_page(self):
        login_page_check = self.browser.find_element(*LoginPageLocators.login_form).text
        assert login_page_check == "Login", "New user registration error"

    def should_be_simple_alert(self, simple_alert):
        get_simple_alert = (self.browser.find_element(*SignInPageLocators.sign_in_email_input_field)
                            .get_attribute("validationMessage"))
        assert get_simple_alert == simple_alert, ("Pop-up notification does not meet requirements "
                                                  "or registration was successful")
