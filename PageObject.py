from BaseApp import BasePage
from Locators import VkLocators

class SearchHelper(BasePage):

    def find_login_button(self):
        button = self.find_element(*VkLocators.VK_LOGIN_BUTTON)
        button.click()
        return button

    def find_field_login(self, word):
        email_field = self.find_element(*VkLocators.VK_EMAIL_FIELD)
        email_field.send_keys(word)
        return email_field

    def find_field_password(self, word):
        pass_field = self.find_element(*VkLocators.VK_PASSWORD_FIELD)
        pass_field.send_keys(word)
        return pass_field

    def find_join_header(self):
        join_header = self.find_element(*VkLocators.VK_JOIN_HEADER)
        return join_header

    def find_capcha_field(self, word):
        find_capcha = self.find_visibility_of_element(*VkLocators.VK_CAPCHA_FIELD)
        find_capcha.send_keys(word)
        return find_capcha

    def find_button_send(self):
        button_send = self.find_element(*VkLocators.VK_CAPCHA_BUTTON)
        button_send.click()
        return button_send

    def check_url(self):
        assert "https://vk.com/" in self.driver.current_url, "Урла не совпадает"

    def check_element(self):
        assert self.is_element_present(*VkLocators.VK_NAME_FIELD), "Поле не найдено"

    def check_that_element_not_displayed(self):
        assert self.is_not_element_present(*VkLocators.VK_NAME_FIELD), "Поле все таки отображается"













