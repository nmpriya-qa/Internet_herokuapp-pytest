import time
import requests
from pagefunctions.BrokenImages import BrokenImages
import utilities.customlogger as lg


class TestBrokenImages:
    log = lg.custom_logger()

    def test_find_broken_images(self, setup_browser):
        self.driver = setup_browser
        self.bi = BrokenImages(self.driver)
        self.bi.go_to_broken_images_page()
        time.sleep(2)
        images = self.bi.get_images()
        broken_images = []
        broken_images_count = 0
        for image in images:
            src1 = image.get_attribute("src")
            self.log.info(f"Image found; {src1}")
            if src1:
                response = requests.get(src1)
                if response.status_code != 200:
                    broken_images.append(image)
                    broken_images_count += 1
                    self.log.info("This is a broken image")
                else:
                    self.log.info("This is not a broken image")
        assert broken_images
        self.log.info(f"Found {broken_images_count} in the broken images page")
