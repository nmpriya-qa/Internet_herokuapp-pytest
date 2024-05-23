from pagefunctions.BasePage import BasePage
import utilities.customlogger as lg


class BrokenImages(BasePage):
    log = lg.custom_logger()

    # Main screen locators to access Broken images page
    __broken_images_link_text = "Broken Images"

    # locators in broken images page
    __images_tag = "img"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def go_to_broken_images_page(self):
        self.click(self.__broken_images_link_text,"link")

    def get_images(self):
        images = self.find_elements(self.__images_tag,"tag")
        return images
