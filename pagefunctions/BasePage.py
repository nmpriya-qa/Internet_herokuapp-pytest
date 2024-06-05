from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementNotVisibleException, NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from traceback import print_stack

import utilities.customlogger as lg

class BasePage:
    log = lg.custom_logger()


    def __init__(self, driver):
        self.driver = driver


    def getlocatortype(self, locatorType):
        locatortype = locatorType.lower()
        if locatortype == "id":
            return By.ID
        elif locatortype == "name":
            return By.NAME
        elif locatortype == "class":
            return By.CLASS_NAME
        elif locatortype == "xpath":
            return By.XPATH
        elif locatortype == "css":
            return By.CSS_SELECTOR
        elif locatortype == "tag":
            return By.TAG_NAME
        elif locatortype == "link":
            return By.LINK_TEXT
        elif locatortype == "plink":
            return By.PARTIAL_LINK_TEXT
        else:
            self.log.error(f"Locator Type: {locatortype} entered is not found")
        return False


    def waitForElement(self, locatorValue, locatortype="id"):
        webElement = None
        try:
            locatorByType = self.getlocatortype(locatortype)
            wait = WebDriverWait(self.driver, 10, poll_frequency=1,
                                 ignored_exceptions=[ElementNotVisibleException, NoSuchElementException])
            webElement = wait.until(ec.presence_of_element_located((locatorByType, locatorValue)))
            self.log.info(f"WebElement found with locator value {locatorValue} using locatorType {locatortype}")
        except:
            self.log.error(f"WebElement not found with locator value {locatorValue} using locatorType {locatortype}")
            print_stack()
            assert False
        return webElement

    def click(self, locatorValue, locatortype="id"):
        try:
            webElement = self.waitForElement(locatorValue, locatortype)
            webElement.click()
            self.log.info(f"Clicked on WebElement with locator value {locatorValue} using locatorType {locatortype}")
        except Exception as e:
            self.log.error(f"Unable to click on WebElement due to {e} with locator value {locatorValue} using locatorType {locatortype}")
            print_stack()
            assert False


    def send_text(self, text, locatorValue, locatortype="id"):
        try:
            webElement = self.waitForElement(locatorValue, locatortype)
            webElement.click()
            webElement.clear()
            webElement.send_keys(text)
            self.log.info(f"Sent the text {text} in WebElement with locator value {locatorValue} using locatorType {locatortype}")
        except:
            self.log.error(f"Unable to send the text {text} in WebElement with locator value {locatorValue} using "
                           f"locatorType {locatortype}")
            print_stack()
            assert False


    def getText(self, locatorValue, locatortype="id"):
        elementText = None
        try:
            webElement = self.waitForElement(locatorValue, locatortype)
            elementText = webElement.text
            self.log.info(
                "Got the text " + elementText + " from WebElement with locator value " + locatorValue + " using locatorType " + locatortype)
        except:
            self.log.error(
                "Unable to get the text " + elementText + " from WebElement with locator value " + locatorValue + "using locatorType " + locatortype)
            print_stack()
        return elementText

    def get_attribute(self, attribute, locatorValue, locatortype="id"):
        element_attribute = None
        try:
            locatortype = locatortype.lower()
            webElement = self.waitForElement(locatorValue, locatortype)
            element_attribute = webElement.get_attribute(attribute)
            # self.log.info(
            #     "Got the attribute " + element_attribute + "for the attribute" + attribute )
        except:
            # self.log.error(
            #     "Unable to get the attribute " + element_attribute + "for the attribute" + attribute)
            print_stack()
        return element_attribute

    def is_element_displayed(self, locatorValue, locatortype):

        try:
            locatorByType = self.getlocatortype(locatortype)
            # Explicitly wait for the element to be visible
            wait = WebDriverWait(self.driver, 10, poll_frequency=1,
                                 ignored_exceptions=[ElementNotVisibleException, NoSuchElementException])
            wait.until(ec.visibility_of_element_located((locatorByType, locatorValue)))
            # If element is found and visible, return True
            self.log.info("Web Element is displayed")
            return True
        except (NoSuchElementException, TimeoutException):
            self.log.info("Web Element not displayed")
            print_stack()
        # If element is not found or not visible, return False
            return False


    def find_elements(self, locatorvalue, locatortype):
        Webelements = None
        try:
            locatorbytype = self.getlocatortype(locatortype)
            WebElements = self.driver.find_elements(locatorbytype, locatorvalue)
            return WebElements
            self.log.info("WebElements found for given locatorvalue " + locatorvalue + "and locator type" + locatortype)
        except:
            self.log.info("No elements found for locator value:" + locatorvalue + "and locatortype " + locatortype)
            print_stack()

    def get_count_of_elements(self, locatorvalue, locatortype):
        try:
            WebElements = self.find_elements(locatorvalue, locatortype)
            count = len(WebElements)
            return count
            self.log.info("Found " + str(count) + "WebElements for given locator value " + locatorvalue + "and locator type" + locatortype)
        except:
            self.log.info("No elements found for locator value:" + locatorvalue + "and locatortype " + locatortype)
            print_stack()