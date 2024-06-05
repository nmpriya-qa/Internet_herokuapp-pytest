from pagefunctions.BasePage import BasePage
import utilities.customlogger as lg


class AddorRemoveElements(BasePage):
    log = lg.custom_logger()

    # Main screen locators to access basic auth page
    __addremove_element_page = "//a[text()='Add/Remove Elements']"

    # Add/remove Elements screen locators
    __add_element_button_xpath = "//button[text()='Add Element']"
    __delete_button_xpath = "//button[text()='Delete']"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def go_to_add_or_remove_element_page(self):
        self.click(self.__addremove_element_page, "xpath")

    def click_add_element(self):
        self.click(self.__add_element_button_xpath, "xpath")

    def get_count_of_delete_buttons(self):
        count = self.get_count_of_elements(self.__delete_button_xpath, "xpath")
        return count

    def click_delete_button(self):
        self.click(self.__delete_button_xpath, "xpath")

    def is_delete_button_present(self):
        return self.is_element_displayed(self.__delete_button_xpath, "xpath")
