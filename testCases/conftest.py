from selenium import webdriver
import pytest


# pytest fixture to initialize driver object before each test and close after completion of the test
@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
        yield driver
        driver.quit()
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        yield driver
        driver.quit()
    else:
        driver = webdriver.Ie()
        yield driver
        driver.quit()


def pytest_addoption(parser):  # This will get the value from CLI /hooks
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):  # This will return the Browser value to setup method
    return request.config.getoption("--browser")


# Pytest HTML Report
# Hook for adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'Hybrid Framework'
    config._metadata['Module Name'] = 'Admin'
    config._metadata['Tester'] = 'Abhishek'


# Hook to delete/modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
