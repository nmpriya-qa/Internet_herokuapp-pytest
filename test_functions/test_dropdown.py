from pagefunctions.Dropdown import Dropdown
from utilities.readproperties import ReadConfig
import pytest


class TestDropdown:
    baseURL = ReadConfig.get_application_url()

    def test_select_option1_by_text(self, setup_browser):
        """
        Test to select option 1 by visible text.

        Steps:
        1. Launches the browser and navigates to the application URL.
        2. Goes to the dropdown page.
        3. Selects Option 1.
        4. Saves a screenshot.
        """
        try:
            self.driver = setup_browser
            self.dd = Dropdown(self.driver)
            self.dd.goto_dropdown_page()
            self.dd.select_option_by_text("Option 1")
            self.driver.save_screenshot('./screenshots/dropdown1.png')
        except Exception as e:
            pytest.fail(f"Test failed with exception: {e}")


    def test_select_option2_by_value(self, setup_browser):
        """
        Test to select option 2 by value.

        Steps:
        1. Launches the browser and navigates to the application URL.
        2. Goes to the dropdown page.
        3. Selects Option 2.
        4. Saves a screenshot.
        """
        try:
            self.driver = setup_browser
            self.dd = Dropdown(self.driver)
            self.dd.goto_dropdown_page()
            self.dd.select_option_by_value("2")
            self.driver.save_screenshot('./screenshots/dropdown2.png')
        except Exception as e:
            pytest.fail(f"Test failed with exception: {e}")
