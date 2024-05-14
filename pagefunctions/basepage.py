from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementNotVisibleException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
from traceback import print_stack

import utilities.logger as lg

class Basepage:
    log = lg.custom_logger1()


    def __init__(self, driver):
        self.driver = driver


    def getlocatortype(self, locatortype):
        locatortype = locatortype.lower()
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
            self.log.error("Locator Type : " + locatortype + " entered is not found")
        return False


    def waitForElement(self, locatorValue, locatortype="id"):
        webElement = None
        try:
            locatortype = locatortype.lower()
            locatorByType = self.getlocatortype(locatortype)
            wait = WebDriverWait(self.driver, 25, poll_frequency=1,
                                 ignored_exceptions=[ElementNotVisibleException, NoSuchElementException])
            webElement = wait.until(ec.presence_of_element_located((locatorByType, locatorValue)))
            self.log.info(
                "WebElement found with locator value " + locatorValue + " using locatorType " + locatortype)
        except:
            self.log.error(
                "WebElement not found with locator value " + locatorValue + " using locatorType " + locatortype)
            print_stack()
            assert False
        return webElement


    def click(self, locatorValue, locatortype="id"):
        try:
            locatortype = locatortype.lower()
            webElement = self.waitForElement(locatorValue, locatortype)
            webElement.click()
            self.log.info(
                "Clicked on WebElement with locator value " + locatorValue + " using locatorType " + locatortype)
        except:
            self.log.error(
                "Unable to Click on WebElement with locator value " + locatorValue + " using locatorType " + locatortype)
            print_stack()
            assert False


    def send_text(self, text, locatorValue, locatortype="id"):
        try:
            locatortype = locatortype.lower()
            webElement = self.waitForElement(locatorValue, locatortype)
            webElement.click()
            webElement.clear()
            webElement.send_keys(text)
            self.log.info(
                "Sent the text " + text + " in WebElement with locator value " + locatorValue + " using locatorType " + locatortype)
        except:
            self.log.error(
                "Unable to Sent the text " + text + " in WebElement with locator value " + locatorValue + "using locatorType " + locatortype)
            print_stack()
            assert False


    def getText(self, locatorValue, locatortype="id"):
        elementText = None
        try:
            locatortype = locatortype.lower()
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
