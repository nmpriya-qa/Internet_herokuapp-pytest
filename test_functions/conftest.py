import pytest
from selenium import webdriver
import chromedriver_autoinstaller

@pytest.fixture(scope='function')
def setup_browser(request):
    browser = request.config.getoption('--browser')

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
    yield driver
    driver.quit()


def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='chrome', help='Browser: chrome, firefox, edge')
@pytest.fixture(scope='function')
def browser(request):
    return request.config.getoption('--browser')



