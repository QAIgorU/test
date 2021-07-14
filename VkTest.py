from PageObject import SearchHelper


def test_find_email(browser):
    vk_email_field = SearchHelper(browser)
    vk_email_field.go_to_site()
    vk_email_field.find_field_login("igor@yandex.ru")
    vk_email_field.find_field_password(123456789)
    vk_email_field.find_login_button()
    text_of_join_header = vk_email_field.find_join_header().text
    assert "Впервые ВКонтакте?" == text_of_join_header, f"Логин баттон не является Впервые ВКонтакте?, а является {text_of_join_header}"


#def test_find_password(browser):
    #vk_password_field = SearchHelper(browser)
    #vk_password_field.go_to_site()
    #vk_password_field.find_field_password(123456789)

#def test_find_button_and_click_login_button(browser):
    #vk_login_page = SearchHelper(browser)
    #vk_login_page.go_to_site()
    #button = vk_login_page.find_login_button()
    #assert "Войти" == button.text, f"Логин баттон не является Войти, а является {button}"
