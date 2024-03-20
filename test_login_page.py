from .pages.data_for_tests import SignUpPageData
from .pages.sign_up_page import SignUpPage
from .pages.login_page import LoginPage
import time


# ToDo добавить все варианты входных данных из чеклиста
def test_positive_login(browser):
    page = SignUpPage(browser, SignUpPageData.link_sign_in_page)
    page.open()
    page.input_email_sign_up("va223wr4mail@mail.ru")
    page.input_name_sign_up("valid_name")
    page.input_password_sign_up(SignUpPageData.random_valid_password)
    page.click_button_sign_up()
    login_page = LoginPage(browser, browser.current_url)
    login_page.input_email_login("va2sfdыап7liwetd_email@mail.ru")
    login_page.input_password_login(SignUpPageData.random_valid_password)
    time.sleep(10)
    login_page.click_button_sign_up()
    #page.should_be_open_login_page()
