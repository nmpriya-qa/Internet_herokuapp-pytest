from pagefunctions.BasePage import BasePage
import utilities.customlogger as lg


class FileUpload(BasePage):
    log = lg.custom_logger()

    # Locators to go to File Upload page
    __file_upload_link_text = "File Upload"

    # Locators in File upload page
    __choose_file_button_css = "#file-upload"
    __upload_submission_button_id = "file-submit"

    # Locators in file upload response page

    __file_upload_response_header_css = "h3"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def go_to_file_upload_page(self):
        self.click(self.__file_upload_link_text, "link")

    def upload_file(self, filepath):
        file_button = self.waitForElement(self.__choose_file_button_css, "css")
        file_button.send_keys(filepath)

    def click_upload_button(self):
        self.click(self.__upload_submission_button_id, "id")

    def get_file_upload_response_text(self):
        response = self.getText(self.__file_upload_response_header_css, "css")
        return response
