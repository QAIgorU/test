from BaseApp import BasePage
from selenium.webdriver.common.by import By

class VkLocators:
    VK_LOGIN_BUTTON = (By.ID, "index_login_button")

class SearchHelper(BasePage):

    def find_login_button(self):
        button = self.find_element(VkLocators.VK_LOGIN_BUTTON)
        button.click
        return button






