from selenium.webdriver.common.by import By
from pagefunctions.BasePage import BasePage


class Checkboxes(BasePage):
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
        checkbox1 = self.driver.find_element(By.XPATH, self.__checkbox1_xpath)
        if checkbox1.is_selected():
            print("Checkbox is already selected")
        else:
            checkbox1.click()
            print("Checkbox is selected")

    def unselect_checkbox1(self):
        checkbox1 = self.driver.find_element(By.XPATH, self.__checkbox1_xpath)
        if checkbox1.is_selected():
            checkbox1.click()
            print("Checkbox is unselected")
        else:
            print("Checkbox is already unselected")

    def select_checkbox2(self):
        checkbox2 = self.driver.find_element(By.XPATH, self.__checkbox2_xpath)
        if checkbox2.is_selected():
            print("Checkbox is already selected")
        else:
            checkbox2.click()
            print("Checkbox is selected")

    def unselect_checkbox2(self):
        checkbox2 = self.driver.find_element(By.XPATH, self.__checkbox2_xpath)
        if checkbox2.is_selected():
            checkbox2.click()
            print("Checkbox is unselected")
        else:
            print("Checkbox is already unselected")
