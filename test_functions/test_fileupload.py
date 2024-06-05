import time
from pagefunctions.FileUpload import FileUpload
import pytest


class TestFileUpload:

    def test_upload_file(self,setup_browser):
        try:
            self.driver = setup_browser
            self.fu = FileUpload(self.driver)
            self.fu.go_to_file_upload_page()
            # For File upload, send the filepath directly in to File upload web element without clicking on it
            self.fu.upload_file("/Users/moorthys/Documents/Priya/resume/Resume-Mohana-Priya-Nagarajan.pdf")
            time.sleep(2)
            self.fu.click_upload_button()
            actual_response = self.fu.get_file_upload_response_text()
            assert actual_response == "File Uploaded!"
        except AssertionError as e:
            pytest.fail(f"Failed due to assertion error: {e}")
        except Exception as e:
            pytest.fail(f"Failed with other reason: {e}")