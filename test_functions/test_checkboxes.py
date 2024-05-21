from pagefunctions.checkboxes import Checkboxes
from utilities.readproperties import ReadConfig
import pytest

class Test_checkboxes:
    baseURL = ReadConfig.get_application_url()

    def test_select_checkbox1(self, setup_browser):
        """
        Test to select checkbox 1.

        Steps:
        1. Launches the browser and navigates to the application URL.
        2. Goes to the checkbox page.
        3. Selects checkbox 1.
        4. Saves a screenshot.
        """
        try:
            self.driver = setup_browser
            self.driver.get(self.baseURL)
            self.cb = Checkboxes(self.driver)
            self.cb.goto_checkbox_page()
            self.cb.select_checkbox1()
            self.driver.save_screenshot('./screenshots/checkbox1.png')

        except Exception as e:
            pytest.fail(f"Test failed with exception: {e}")

    def test_unselect_checkbox2(self, setup_browser):
        """
        Test to unselect checkbox 2.

        Steps:
        1. Launches the browser and navigates to the application URL.
        2. Goes to the checkbox page.
        3. Selects checkbox 1.
        4. Saves a screenshot.
        """
        try:
            self.driver = setup_browser
            self.driver.get(self.baseURL)
            self.cb = Checkboxes(self.driver)
            self.cb.goto_checkbox_page()
            self.cb.unselect_checkbox2()
            self.driver.save_screenshot('./screenshots/checkbox2.png')
        except Exception as e:
            pytest.fail(f"Test failed with exception: {e}")

