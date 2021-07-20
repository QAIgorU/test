from PageObject import SearchHelper
import pytest

@pytest.mark.smoke
def test_find_email(browser):
    vk_email_field = SearchHelper(browser)
    vk_email_field.go_to_site()
    vk_email_field.find_field_login("igor@yandex.ru")
    vk_email_field.find_field_password("123456789")
    vk_email_field.find_login_button()
    vk_email_field.find_capcha_field("Hello")
    vk_email_field.find_button_send()

def test_find_field_name(browser):
    find_user_name_field = SearchHelper(browser)
    find_user_name_field.go_to_site()
    find_user_name_field.check_element()
    find_user_name_field.check_url()

def test_naiti_pole(browser):
    pole_naiti = SearchHelper(browser)
    pole_naiti.go_to_site()
    pole_naiti.check_that_element_not_displayed()



