from selenium.webdriver.common.by import By
from pagefunctions.basepage import Basepage
import utilities.logger as lg


class BasicAuth(Basepage):
    log = lg.custom_logger1()

    # Main screen locators to access basic auth page
    __basic_auth_linktext = "Basic Auth"

    # Basic auth screen locators
    basic_auth_header_xpath = "//h3[text()='Basic Auth']"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def goto_basic_auth(self):
        self.driver.find_element(By.LINK_TEXT, self.__basic_auth_linktext).click()

    def basic_auth_login_url(self, user, pwd):
        basic_auth_extended_link = self.get_attribute("href", self.__basic_auth_linktext, 'link')
        link_split = basic_auth_extended_link.split('//')
        new_url = f"{link_split[0]}//{user}:{pwd}@{link_split[1]}"
        self.log.info("URL for Basic Auth with credentials is " + new_url)
        return new_url

    def get_basic_auth_header_text(self):
        text = self.getText(self.basic_auth_header_xpath, "xpath")
        return text

