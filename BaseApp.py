from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://vk.com/"

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator{locator}")

    def go_to_site(self):
        return self.driver.get(self.base_url)

    def switch_to_window(self):
        new_window = self.driver.window_handles[1]
        return self.driver.switch_to.window(new_window)












