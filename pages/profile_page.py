from .base_page import BasePage
from .locators import ProfilePageLocators


class ProfilePage(BasePage):

    def should_be_open_profile_page(self, name):
        profile_text_page = self.browser.find_element(*ProfilePageLocators.profile_text_page).text == f"Welcome, {name}!"
        assert profile_text_page, f"Incorrect message on profile page waiting for: Welcome, {name}!"

    def should_be_open_profile_page_without_name(self):
        profile_text_page = self.browser.find_element(*ProfilePageLocators.profile_text_page).text == "Welcome!"
        assert profile_text_page, "Incorrect message on profile page waiting for: Welcome!"
