from selenium.webdriver.common.by import By

class VkLocators():
    VK_LOGIN_BUTTON = (By.ID, "index_login_button")
    VK_EMAIL_FIELD = (By.ID, "index_email")
    VK_PASSWORD_FIELD = (By.ID, "index_pass")
    VK_JOIN_HEADER = (By.CSS_SELECTOR, "[class='JoinForm__header']")
    VK_CAPCHA_FIELD = (By.XPATH, "//div[@class='box_layout']//input[@class='big_text']")
    VK_CAPCHA_BUTTON = (By.XPATH, "//div[@class='box_layout']//button[@class='flat_button']")
    VK_NAME_FIELD = (By.CSS_SELECTOR, "[name='first_name']")