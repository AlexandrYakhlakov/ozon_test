import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--driver', default='chrome')


@pytest.fixture()
def driver(request):
    driver = request.config.getoption('--driver')
    if driver == 'chrome':
        driver = webdriver.Chrome()
    elif driver == 'firefox':
        driver = webdriver.Firefox()
    elif driver == 'opera':
        driver = webdriver.Opera()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()
