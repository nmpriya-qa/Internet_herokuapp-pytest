from pagefunctions.BasicAuth import BasicAuth
from utilities.readproperties import ReadConfig
import pytest
import time

class TestBasicAuth:
    base_url = ReadConfig.get_application_url()
    user = ReadConfig.basic_auth_user()
    pwd = ReadConfig.basic_auth_pwd()



    def test_basic_auth_valid_credentials(self, setup_browser):

        try:
            self.driver = setup_browser
            self.driver.get(self.base_url)
            self.ba = BasicAuth(self.driver)
            basic_auth_url = self.ba.basic_auth_login_url(self.user, self.pwd)
            self.driver.execute_script("window.open();")
            self.driver.switch_to.window(self.driver.window_handles[1])
            self.driver.get(basic_auth_url)
            actual_text = self.ba.get_basic_auth_header_text()
            assert actual_text == "Basic Auth"
        except AssertionError as 
