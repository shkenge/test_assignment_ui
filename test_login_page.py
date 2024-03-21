import pytest
from .pages.data_for_tests import SignUpPageData
from .pages.data_for_tests import LogInPageData
from .pages.data_for_tests import ProfilePageData
from .pages.profile_page import ProfilePage
from .pages.sign_up_page import SignUpPage
from .pages.login_page import LoginPage


# ToDo добавить все варианты входных данных из чеклиста
@pytest.mark.parametrize("input", [
    LogInPageData.lower_case_all_fields, LogInPageData.upper_case_all_fields],
                         ids=["lower_case", "upper_case"])
def test_positive_login(browser, input):
    page = SignUpPage(browser, SignUpPageData.link_sign_in_page)
    page.open()
    page.sign_up(*input)
    login_page = LoginPage(browser, LogInPageData.link_log_in_page)
    login_page.login(input[0], input[2])
    profile_page = ProfilePage(browser, ProfilePageData.link_profile_page)
    profile_page.should_be_open_profile_page(input[1])


def test_positive_login_with_different_case(browser):
    page = SignUpPage(browser, SignUpPageData.link_sign_in_page)
    page.open()
    page.sign_up(*LogInPageData.lower_case_all_fields)
    login_page = LoginPage(browser, LogInPageData.link_log_in_page)
    login_page.login(LogInPageData.lower_case_all_fields[0].upper(), LogInPageData.lower_case_all_fields[2])
    profile_page = ProfilePage(browser, ProfilePageData.link_profile_page)
    profile_page.should_be_open_profile_page(LogInPageData.lower_case_all_fields[1])


def test_negative_login_with_wrong_email(browser):
    login_page = LoginPage(browser, LogInPageData.link_log_in_page)
    login_page.open()
    login_page.login(*LogInPageData.login_and_password_with_no_name)
    login_page.should_not_log_in()


def test_negative_login_with_wrong_password(browser):
    page = SignUpPage(browser, SignUpPageData.link_sign_in_page)
    page.open()
    page.sign_up_without_name(*LogInPageData.login_and_password_with_no_name)
    login_page = LoginPage(browser, LogInPageData.link_log_in_page)
    login_page.login(LogInPageData.login_and_password_with_no_name[0], 'wrong_password')
    login_page.should_not_log_in()


def test_positive_login_without_name(browser):
    page = SignUpPage(browser, SignUpPageData.link_sign_in_page)
    page.open()
    page.sign_up_without_name(*LogInPageData.login_and_password_with_no_name)
    login_page = LoginPage(browser, LogInPageData.link_log_in_page)
    login_page.login(*LogInPageData.login_and_password_with_no_name)
    profile_page = ProfilePage(browser, ProfilePageData.link_profile_page)
    profile_page.should_be_open_profile_page_without_name()
