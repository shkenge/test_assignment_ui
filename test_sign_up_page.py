import pytest
from .pages.data_for_tests import SignUpPageData
from .pages.sign_up_page import SignUpPage


@pytest.mark.parametrize("input_email", [
    SignUpPageData.lower_case_email, SignUpPageData.upper_case_email,
    SignUpPageData.camel_case_email, SignUpPageData.cyrillic_in_domain,
    SignUpPageData.numbers_in_name_email, SignUpPageData.numbers_in_domain,
    SignUpPageData.hyphen_in_email_name, SignUpPageData.hyphen_in_domain,
    SignUpPageData.underscore_in_email_name, SignUpPageData.with_dot_in_email_name,
    SignUpPageData.email_with_1_char_in_email_name, SignUpPageData.email_with_200_chars_in_email_name,
    SignUpPageData.email_with_4_domain_levels, SignUpPageData.first_level_domain_2_chars_after_dot,
    SignUpPageData.first_level_domain_10_chars_after_dot, SignUpPageData.first_level_domain_63_chars_after_dot
], ids=["lower_case_email", "upper_case_email",
        "camel_case_email", "cyrillic_in_domain",
        "numbers_in_name_email", "numbers_in_domain",
        "hyphen_in_email_name", "hyphen_in_domain",
        "underscore_in_email_name", "with_dot_in_email_name",
        "email_with_1_char_in_email_name", "email_with_200_chars_in_email_name",
        "email_with_4_domain_levels", "first_level_domain_2_char_after_dot",
        "first_level_domain_10_char_after_dot", "first_level_domain_63_char_after_dot"])
def test_positive_input_email(browser, input_email):
    page = SignUpPage(browser, SignUpPageData.link_sign_in_page)
    page.open()
    page.sign_up(input_email, '', SignUpPageData.input_random_password)
    page.should_be_open_login_page()


@pytest.mark.parametrize("input_email, simple_alert", [
    (SignUpPageData.email_with_underscore_in_domain, SignUpPageData.alert_email_with_underscore_in_domain),
    (SignUpPageData.email_empty_field, SignUpPageData.alert_email_empty_field),
    (SignUpPageData.email_with_several_dots_in_row_in_domain, SignUpPageData.alert_email_with_several_dots_in_row_in_domain),
    (SignUpPageData.email_without_first_level_domain, SignUpPageData.alert_email_without_first_level_domain),
    (SignUpPageData.email_without_second_level_domain, SignUpPageData.alert_email_without_second_level_domain),
    (SignUpPageData.email_without_dots_in_domain, SignUpPageData.alert_email_without_dots_in_domain),
    (SignUpPageData.email_500_chars, SignUpPageData.alert_email_500_chars),
    (SignUpPageData.email_lack_at_symbol, SignUpPageData.alert_email_lack_at_symbol),
    (SignUpPageData.email_with_two_at_symbol, SignUpPageData.alert_email_with_two_at_symbol),
    (SignUpPageData.email_with_spaces_in_middle_name, SignUpPageData.alert_email_with_spaces_in_middle_name),
    (SignUpPageData.email_with_spaces_in_beginning_domain, SignUpPageData.alert_email_with_spaces_in_beginning_domain),
    (SignUpPageData.email_with_spaces_in_middle_domain, SignUpPageData.alert_email_with_spaces_in_middle_domain),
    (SignUpPageData.email_without_name, SignUpPageData.alert_email_without_name),
    (SignUpPageData.email_without_domain, SignUpPageData.alert_email_without_domain),
    (SignUpPageData.email_first_level_domain_1_char, SignUpPageData.alert_email_first_level_domain_1_char),
    (SignUpPageData.email_first_level_domain_64_chars, SignUpPageData.alert_email_first_level_domain_64_chars),
    (SignUpPageData.email_cyrillic_in_name, SignUpPageData.alert_email_cyrillic_in_name)
], ids=["email_with_underscore_in_domain",
        "email_empty_field",
        "email_with_several_dots_in_row_in_domain",
        "email_without_first_level_domain",
        "email_without_second_level_domain",
        "without_dots_in_domain",
        "email_500_chars",
        "email_lack_at_symbol",
        "email_with_two_at_symbol",
        "email_with_spaces_in_middle_name",
        "email_with_spaces_in_beginning_domain",
        "email_with_spaces_in_middle_domain",
        "email_without_name",
        "email_without_domain",
        "email_first_level_domain_1_char",
        "email_first_level_domain_64_chars",
        "email_cyrillic_in_name"])
def test_negative_input_email(browser, input_email, simple_alert):
    page = SignUpPage(browser, SignUpPageData.link_sign_in_page, 10)
    page.open()
    page.sign_up(input_email, '', SignUpPageData.input_random_password)
    page.should_be_simple_alert(simple_alert)
