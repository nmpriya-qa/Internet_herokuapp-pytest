from pagefunctions.AddOrRemoveElements import AddorRemoveElements
from utilities.readproperties import ReadConfig
import pytest
import utilities.customlogger as lg
import time


class TestBasicAuth:
    log = lg.custom_logger()
    no_of_delete_buttons = ReadConfig.no_of_clicks_add_element()

    def test_add_element_once(self, setup_browser):
        """ Go to basic auth page with valid credentials"""
        try:
            self.driver = setup_browser
            self.are = AddorRemoveElements(self.driver)
            self.are.go_to_add_or_remove_element_page()
            time.sleep(2)
            self.are.click_add_element()
            delete_button_count = self.are.get_count_of_delete_buttons()
            self.log.info(f"Delete button count is {delete_button_count}")
            assert delete_button_count == 1
        except AssertionError as msg:
            pytest.fail(f"failed with msg {msg}")

    def test_add_and_delete_element_once(self, setup_browser):
        try:
            self.driver = setup_browser
            self.are = AddorRemoveElements(self.driver)
            self.are.go_to_add_or_remove_element_page()
            self.are.click_add_element()
            delete_button_count = self.are.get_count_of_delete_buttons()
            assert delete_button_count == 1
            self.are.click_delete_button()
            assert not self.are.is_delete_button_present()
        except AssertionError as msg:
            pytest.fail(f"failed with msg {msg}")

    def test_add_multiple_elements(self, setup_browser):
        i = 1
        try:
            self.driver = setup_browser
            self.are = AddorRemoveElements(self.driver)
            self.are.go_to_add_or_remove_element_page()
            while i <= self.no_of_delete_buttons:
                self.are.click_add_element()
                i += 1
                self.log.info(f"add: {i}")
            delete_button_count = self.are.get_count_of_delete_buttons()
            self.log.info(f"Delete button count is {delete_button_count}")
            assert delete_button_count == self.no_of_delete_buttons
            while self.are.is_delete_button_present():
                self.are.click_delete_button()
        except AssertionError as msg:
            pytest.fail(f"failed with msg {msg}")
