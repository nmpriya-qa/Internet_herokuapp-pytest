import pytest
from selenium import webdriver
from utilities.readproperties import ReadConfig

@pytest.fixture(scope='function')
def setup_browser(request):
    browser = request.config.getoption('--browser')
    application_url = ReadConfig.get_application_url()

    if browser == 'chrome':
        # chromedriver_autoinstaller.install()
        driver = webdriver.Chrome()
        print("Launching Chrome browser")
    elif browser == 'edge':
        driver = webdriver.Edge()
        print("Launching Chrome browser")
    else:
        driver = webdriver.Chrome  # default
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get(application_url)
    yield driver
    driver.quit()


def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='chrome', help='Browser: chrome, firefox, edge')
@pytest.fixture(scope='function')
def browser(request):
    return request.config.getoption('--browser')



