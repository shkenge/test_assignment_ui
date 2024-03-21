from ..helpers import TestMethods


class MainPageData:
    link_main_page = "http://localhost:5000/"
    window_size_1920_1080 = (1920, 1080)
    window_size_960_540 = (960, 540)
    window_size_320_569 = (320, 569)


class LogInPageData:
    link_log_in_page = "http://localhost:5000/login"
    error_notification = "Please check your login details and try again."
    lower_case_all_fields = ((f"{TestMethods.get_random_string(10)}@{TestMethods.get_random_string(4)}."f"{TestMethods.get_random_string(2)}").lower(),
                             (f"{TestMethods.get_random_string(10)}").lower(),
                             (f"{TestMethods.get_random_string(10)}").lower())
    upper_case_all_fields = (f"{TestMethods.get_random_string(10)}@{TestMethods.get_random_string(4)}."f"{TestMethods.get_random_string(2)}",
                             f"{TestMethods.get_random_string(10)}",
                             f"{TestMethods.get_random_string(10)}")
    login_and_password_with_no_name = ((f"{TestMethods.get_random_string(10)}@{TestMethods.get_random_string(4)}."f"{TestMethods.get_random_string(2)}").lower(),
                          (f"{TestMethods.get_random_string(10)}").lower())


class SignUpPageData:
    link_sign_in_page = "http://localhost:5000/signup"
    input_random_email = (f"{TestMethods.get_random_string(10)}@{TestMethods.get_random_string(4)}."
                          f"{TestMethods.get_random_string(2)}").lower()
    input_random_name_email = TestMethods.get_random_string(10).lower()
    input_random_first_level_domain_email = f"{TestMethods.get_random_string(2)}".lower()
    input_random_second_level_domain_email = f"{TestMethods.get_random_string(4)}".lower()
    input_random_name = f"{TestMethods.get_random_string(8)}{TestMethods.get_random_numbers(1999)}".lower()
    input_random_password = f"{TestMethods.get_random_string(8)}{TestMethods.get_random_numbers(1999)}"

    lower_case_email = (f"{TestMethods.get_random_string(10)}@{TestMethods.get_random_string(4)}."
                        f"{TestMethods.get_random_string(2)}").lower()
    upper_case_email = (f"{TestMethods.get_random_string(10)}@{TestMethods.get_random_string(4)}."
                        f"{TestMethods.get_random_string(2)}").upper()
    camel_case_email = (f"Tes{TestMethods.get_random_string(5)}Te@{TestMethods.get_random_string(2)}il."
                        f"r{TestMethods.get_random_string(1)}")
    cyrillic_in_domain = f"{TestMethods.get_random_string(10)}@почта.рф"
    numbers_in_name_email = (f"{TestMethods.get_random_numbers(1999)}{TestMethods.get_random_string(5)}@"
                             f"{TestMethods.get_random_string(4)}.{TestMethods.get_random_string(2)}").lower()
    numbers_in_domain = (f"{TestMethods.get_random_string(10)}@{TestMethods.get_random_numbers(199)}"
                         f"{TestMethods.get_random_string(2)}.{TestMethods.get_random_string(2)}").lower()
    hyphen_in_email_name = (f"{TestMethods.get_random_string(5)}-{TestMethods.get_random_string(5)}@"
                            f"{TestMethods.get_random_string(4)}.{TestMethods.get_random_string(2)}").lower()
    hyphen_in_domain = (f"{TestMethods.get_random_string(5)}@{TestMethods.get_random_string(2)}-"
                        f"{TestMethods.get_random_string(2)}.{TestMethods.get_random_string(2)}").lower()
    underscore_in_email_name = (f"{TestMethods.get_random_string(5)}_{TestMethods.get_random_string(5)}@"
                                f"{TestMethods.get_random_string(4)}.{TestMethods.get_random_string(2)}").lower()
    with_dot_in_email_name = (f"{TestMethods.get_random_string(5)}.{TestMethods.get_random_string(5)}@"
                              f"{TestMethods.get_random_string(4)}.{TestMethods.get_random_string(2)}").lower()
    email_with_1_char_in_email_name = (f"{TestMethods.get_random_string(1)}@{TestMethods.get_random_string(4)}."
                                       f"{TestMethods.get_random_string(2)}").lower()
    email_with_200_chars_in_email_name = (f"{TestMethods.get_random_string(200)}@{TestMethods.get_random_string(4)}."
                                          f"{TestMethods.get_random_string(2)}").lower()
    email_with_4_domain_levels = (f"{TestMethods.get_random_string(10)}@{TestMethods.get_random_string(4)}."
                                  f"{TestMethods.get_random_string(2)}.{TestMethods.get_random_string(2)}."
                                  f"{TestMethods.get_random_string(2)}").lower()
    first_level_domain_2_chars_after_dot = (f"{TestMethods.get_random_string(10)}@{TestMethods.get_random_string(4)}."
                                            f"{TestMethods.get_random_string(2)}").lower()
    first_level_domain_10_chars_after_dot = (f"{TestMethods.get_random_string(10)}@{TestMethods.get_random_string(4)}."
                                             f"{TestMethods.get_random_string(10)}").lower()
    first_level_domain_63_chars_after_dot = (f"{TestMethods.get_random_string(10)}@{TestMethods.get_random_string(4)}."
                                             f"{TestMethods.get_random_string(63)}").lower()
    email_with_spaces_beginning_name = (f"   {TestMethods.get_random_string(10)}@{TestMethods.get_random_string(4)}."
                                        f"{TestMethods.get_random_string(2)}").lower()
    email_with_spaces_end_name = (f"{TestMethods.get_random_string(10)}@{TestMethods.get_random_string(4)}."
                                  f"{TestMethods.get_random_string(2)}   ").lower()
    email_with_spaces_in_end_domain = (f"{TestMethods.get_random_string(10)}@{TestMethods.get_random_string(2)}  "
                                       f"{TestMethods.get_random_string(2)}.{TestMethods.get_random_string(2)}").lower()

    email_with_underscore_in_domain = (f"{TestMethods.get_random_string(10)}@{TestMethods.get_random_string(4)}_"
                                       f"{TestMethods.get_random_string(2)}.{TestMethods.get_random_string(2)}").lower()
    alert_email_with_underscore_in_domain = 'Часть адреса после символа "@" не должна содержать символ "_".'
    email_empty_field = ""
    alert_email_empty_field = "Уточнить какое сообщение должно появляться"
    email_with_several_dots_in_row_in_domain = (f'{TestMethods.get_random_string(10)}@'
                                                f'{input_random_second_level_domain_email}..'
                                                f'{input_random_first_level_domain_email}').lower()
    alert_email_with_several_dots_in_row_in_domain = (f'Недопустимое положение символа "." в адресе '
                                                      f'"{input_random_second_level_domain_email}..'
                                                      f'{input_random_first_level_domain_email}".')
    email_without_first_level_domain = (f'{TestMethods.get_random_string(10)}@'
                                        f'{input_random_first_level_domain_email}.').lower()
    alert_email_without_first_level_domain = (f'Недопустимое положение символа "." '
                                              f'в адресе "{input_random_first_level_domain_email}.".')
    email_without_second_level_domain = (f"{TestMethods.get_random_string(10)}@"
                                         f".{input_random_second_level_domain_email}").lower()
    alert_email_without_second_level_domain = (f'Недопустимое положение символа "." в адресе '
                                               f'".{input_random_second_level_domain_email}".')
    email_without_dots_in_domain = (f"{TestMethods.get_random_string(10)}@{TestMethods.get_random_string(4)}"
                                    f"{TestMethods.get_random_string(2)}").lower()
    alert_email_without_dots_in_domain = "Уточнить какое сообщение должно появляться"
    email_500_chars = (f"{TestMethods.get_random_string(500)}@{TestMethods.get_random_string(4)}."
                       f"{TestMethods.get_random_string(2)}").lower()
    alert_email_500_chars = "Уточнить какое сообщение должно появляться"
    email_lack_at_symbol = (f"{TestMethods.get_random_string(10)}{TestMethods.get_random_string(4)}."
                            f"{TestMethods.get_random_string(2)}").lower()
    alert_email_lack_at_symbol = (f'Адрес электронной почты должен содержать символ "@". '
                                  f'В адресе "{email_lack_at_symbol}" отсутствует символ "@".')
    email_with_two_at_symbol = (f"{TestMethods.get_random_string(10)}@@{TestMethods.get_random_string(4)}."
                                f"{TestMethods.get_random_string(2)}").lower()
    alert_email_with_two_at_symbol = 'Часть адреса после символа "@" не должна содержать символ "@".'
    email_with_spaces_in_middle_name = (f"{TestMethods.get_random_string(5)}   {TestMethods.get_random_string(5)}@"
                                        f"{TestMethods.get_random_string(4)}."
                                        f"{TestMethods.get_random_string(2)}").lower()
    alert_email_with_spaces_in_middle_name = 'Часть адреса до символа "@" не должна содержать символ " ".'
    email_with_spaces_in_beginning_domain = (f"{TestMethods.get_random_string(10)}@   "
                                             f"{TestMethods.get_random_string(4)}."
                                             f"{TestMethods.get_random_string(2)}").lower()
    alert_email_with_spaces_in_beginning_domain = 'Часть адреса после символа "@" не должна содержать символ " ".'
    email_with_spaces_in_middle_domain = (f"{TestMethods.get_random_string(10)}@"
                                          f"{TestMethods.get_random_string(4)}   ."
                                          f"{TestMethods.get_random_string(2)}").lower()
    alert_email_with_spaces_in_middle_domain = 'Часть адреса после символа "@" не должна содержать символ " ".'
    email_without_name = (f"@{TestMethods.get_random_string(4)}."
                          f"{TestMethods.get_random_string(2)}").lower()
    alert_email_without_name = (f'Введите часть адреса до символа "@". '
                                f'Адрес "{email_without_name}" неполный.')
    email_without_domain = f"{TestMethods.get_random_string(10)}@".lower()
    alert_email_without_domain = (f'Введите часть адреса после символа "@". '
                                  f'Адрес "{email_without_domain}" неполный.')
    email_first_level_domain_1_char = (f"{TestMethods.get_random_string(10)}@{TestMethods.get_random_string(4)}."
                                       f"{TestMethods.get_random_string(1)}").lower()
    alert_email_first_level_domain_1_char = "Уточнить какое сообщение должно появляться"
    email_first_level_domain_64_chars = (f"{TestMethods.get_random_string(10)}@{TestMethods.get_random_string(4)}."
                                         f"{TestMethods.get_random_string(64)}").lower()
    alert_email_first_level_domain_64_chars = "Уточнить какое сообщение должно появляться"
    email_cyrillic_in_name = (f"{TestMethods.get_random_string(6)}тест@{TestMethods.get_random_string(4)}."
                              f"{TestMethods.get_random_string(2)}").lower()
    alert_email_cyrillic_in_name = 'Часть адреса до символа "@" не должна содержать символ "т".'


input_random_name_email = TestMethods.get_random_string(10).lower()
input_random_first_level_domain_email = f"{TestMethods.get_random_string(2)}".lower()
input_random_second_level_domain_email = f"{TestMethods.get_random_string(4)}".lower()
input_random_name = f"{TestMethods.get_random_string(8)}{TestMethods.get_random_numbers(1999)}".lower()
input_random_password = f"{TestMethods.get_random_string(8)}{TestMethods.get_random_numbers(1999)}"
email_with_several_dots_in_row_in_domain = (f'{TestMethods.get_random_string(10)}@'
                                            f'{input_random_second_level_domain_email}..'
                                            f'{input_random_first_level_domain_email}').lower()
alert_email_with_several_dots_in_row_in_domain = (f'Недопустимое положение символа "." в адресе '
                                                  f'"{input_random_second_level_domain_email}..'
                                                  f'{input_random_first_level_domain_email}".')


class ProfilePageData:
    link_profile_page = "http://localhost:5000/profile"
