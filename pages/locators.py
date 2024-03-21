from selenium.webdriver.common.by import By


class MainPageLocators:
    main_page_text = (By.CSS_SELECTOR, ".title")
    nav_bar_menu = (By.ID, "navbarMenuHeroA")
    button_home = (By.CSS_SELECTOR, '[href="/"]')
    button_login = (By.CSS_SELECTOR, '[href="/login"]')
    button_signup = (By.CSS_SELECTOR, '[href="/signup"]')


class LoginPageLocators:
    login_form = (By.CSS_SELECTOR, '.title')
    login_email_input_field = (By.NAME, 'email')
    login_password_input_field = (By.NAME, 'password')
    login_checkbox_remember_me = (By.CSS_SELECTOR, '[type="checkbox"]')
    login_button = (By.CSS_SELECTOR, '.button.is-block.is-info')
    notification = (By.CSS_SELECTOR, '.notification.is-danger')


class SignInPageLocators:
    sign_in_form = (By.CSS_SELECTOR, ".title")
    sign_in_email_input_field = (By.NAME, 'email')
    sign_in_email_input_name = (By.NAME, 'name')
    sign_in_password_input_field = (By.NAME, 'password')
    sign_in_checkbox_remember_me = (By.CSS_SELECTOR, '[type="checkbox"]')
    sign_in_button = (By.CSS_SELECTOR, '.button.is-block.is-info')


class ProfilePageLocators:
    profile_text_page = (By.CSS_SELECTOR, ".title")
    profile_logout_button = (By.CSS_SELECTOR, '[href="/logout"]')
