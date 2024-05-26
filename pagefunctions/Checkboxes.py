from pagefunctions.BasePage import BasePage
import utilities.customlogger as lg


class Checkboxes(BasePage):
    log = lg.custom_logger()

    # locators - main page
    __checkboxes_link_text = "Checkboxes"
    # locators - inside checkboxes page
    __checkbox1_xpath = "//form[@id='checkboxes']/input[1]"
    __checkbox2_xpath = "//form[@id='checkboxes']/input[2]"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def goto_checkbox_page(self):
        self.click(self.__checkboxes_link_text, "link")

    def select_checkbox1(self):
        checkbox1 = self.waitForElement(self.__checkbox1_xpath, "xpath")
        if checkbox1.is_selected():
            self.log.info("Checkbox is already selected")
        else:
            checkbox1.click()
            self.log.info("Checkbox is selected")

    def unselect_checkbox1(self):
        checkbox1 = self.waitForElement(self.__checkbox1_xpath, "xpath")
        if checkbox1.is_selected():
            checkbox1.click()
            self.log.info("Checkbox is unselected")
        else:
            self.log.info("Checkbox is already unselected")

    def select_checkbox2(self):
        checkbox2 = self.waitForElement(self.__checkbox2_xpath, "xpath")
        if checkbox2.is_selected():
            self.log.info("Checkbox is already selected")
        else:
            checkbox2.click()
            self.log.info("Checkbox is selected")

    def unselect_checkbox2(self):
        checkbox2 = self.waitForElement(self.__checkbox2_xpath, "xpath")
        if checkbox2.is_selected():
            checkbox2.click()
            self.log.info("Checkbox is unselected")
        else:
            self.log.info("Checkbox is already unselected")
