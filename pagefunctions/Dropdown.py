from pagefunctions.BasePage import BasePage
from selenium.webdriver.support.ui import Select
import utilities.customlogger as lg


class Dropdown(BasePage):
    log = lg.custom_logger()

    # locators - main page
    __dropdown_link_text = "Dropdown"
    # locators - inside Dropdown page
    __dropdown_id = "dropdown"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def goto_dropdown_page(self):
        self.click(self.__dropdown_link_text, "link")

    def select_option_by_text(self,option_text):
        dropdown = self.waitForElement(self.__dropdown_id, "id")
        select = Select(dropdown)
        select.select_by_visible_text(option_text)

    def select_option_by_value(self,value):
        dropdown = self.waitForElement(self.__dropdown_id, "id")
        select = Select(dropdown)
        select.select_by_value(value)
    




