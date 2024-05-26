from pagefunctions.BasePage import BasePage
from selenium.webdriver.common.action_chains import ActionChains
import utilities.customlogger as lg


class DragAndDrop(BasePage):
    log = lg.custom_logger()

    # Locators to go to Drag and drop page
    __drag_and_drop_link_text = "Drag and Drop"

    # Locators inside Drag and drop page
    __column_a_xpath = "//div[@id='column-a']"
    __column_a_header_xpath = "//div[@id='column-a']/header"
    __column_b_xpath = "//div[@id='column-b']"
    __column_b_header_xpath = "//div[@id='column-b']/header"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def go_to_drag_and_drop_page(self):
        self.click(self.__drag_and_drop_link_text, "link")

    def drag_column_a_to_b(self):
        source_element = self.waitForElement(self.__column_a_xpath, "xpath")
        target_element = self.waitForElement(self.__column_b_xpath, "xpath")
        action = ActionChains(self.driver)
        action.drag_and_drop(source_element, target_element).perform()

    def get_column_a_header(self):
        attr_value = self.get_attribute("header", self.__column_a_header_xpath, "xpath")
        return attr_value

    def get_column_b_header(self):
        attr_value = self.getText(self.__column_b_header_xpath, "xpath")
        return attr_value
