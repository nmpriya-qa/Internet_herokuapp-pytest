from pagefunctions.BasicAuth import BasicAuth
from utilities.readproperties import ReadConfig
import pytest


class TestBasicAuth:
    valid_user = ReadConfig.basic_auth_valid_user()
    valid_pwd = ReadConfig.basic_auth_valid_pwd()
    invalid_user = ReadConfig.basic_auth_invalid_user()
    invalid_pwd = ReadConfig.basic_auth_invalid_pwd()



    def test_basic_auth_valid_credentials(self, setup_browser):
        """ Go to basic auth page with valid credentials"""
        try:
            self.driver = setup_browser
            self.ba = BasicAuth(self.driver)
            basic_auth_url = self.ba.basic_auth_login_url(self.valid_user, self.valid_pwd)
            self.driver.execute_script("window.open();")
            self.driver.switch_to.window(self.driver.window_handles[1])
            self.driver.get(basic_auth_url)
            actual_text = self.ba.get_basic_auth_header_text()
            assert actual_text == "Basic Auth"
        except AssertionError as msg:
            pytest.fail()

    def test_basic_auth_invalid_credentials(self, setup_browser):
        """ Go to basic auth page with invalid credentials
            """

        try:
            self.driver = setup_browser
            self.ba = BasicAuth(self.driver)
            basic_auth_url = self.ba.basic_auth_login_url(self.invalid_user, self.invalid_pwd)
            self.driver.execute_script("window.open();")
            self.driver.switch_to.window(self.driver.window_handles[1])
            self.driver.get(basic_auth_url)
            header = self.ba.get_basic_auth_header_text()
            assert header == False
        except AssertionError as msg:
            pytest.fail(f"failed with msg {msg}")