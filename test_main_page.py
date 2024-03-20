import pytest
from .pages.main_page import MainPage
from .pages.locators import MainPageLocators
from .pages.data_for_tests import MainPageData, LogInPageData, SignUpPageData


# def test_text_main_page(browser):
#     page = MainPage(browser, MainPageData.link_main_page)
#     page.open()
#     page.should_be_text_main_page()
#
#
# @pytest.mark.parametrize("click_button, check_url", [
#     (MainPageLocators.button_home, MainPageData.link_main_page),
#     (MainPageLocators.button_login, LogInPageData.link_log_in_page),
#     (MainPageLocators.button_signup, SignUpPageData.link_sign_in_page)
# ], ids=["test_button_home_page", "test_button_log_in", "test_button_signup"])
# def test_navigation_bar_buttons(browser, click_button, check_url):
#     page = MainPage(browser, MainPageData.link_main_page)
#     page.open()
#     page.click_button_navigator_bar(click_button)
#     get_url = browser.current_url
#     page.should_be_open_page(get_url, check_url)


@pytest.mark.parametrize("size_window", [
    MainPageData.window_size_320_569,
    MainPageData.window_size_960_540,
    MainPageData.window_size_1920_1080
], ids=[MainPageData.window_size_320_569.__str__(),
        MainPageData.window_size_960_540.__str__(),
        MainPageData.window_size_1920_1080.__str__()])
def test_navigation_buttons_when_resizing_window(browser, size_window):
    page = MainPage(browser, MainPageData.link_main_page)
    page.open()
    browser.set_window_size(*size_window)
    navigator_bar = page.get_navigator_bar()
    page.should_be_navigator_bar(navigator_bar)
