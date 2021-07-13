from PageObject import SearchHelper

def test_find_button_and_click_login_button(browser):
    vk_login_page = SearchHelper(browser)
    vk_login_page.go_to_site()
    button = vk_login_page.find_login_button().text
    assert button == "Войти", f"Логин баттон не является Войти, а является {button}"