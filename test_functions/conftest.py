import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from utilities.readproperties import ReadConfig


@pytest.fixture(scope='function')
def setup_browser(request):
    application_url = ReadConfig.get_application_url()
    # setting chrome browser
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920x1080")
    driver = webdriver.Chrome(options=chrome_options)
    print("Launching Chrome browser")
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get(application_url)
    yield driver
    driver.quit()




