# import lib
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


# browser = Service("./drivers/chromedriver.exe")


# @pytest.fixture()
# def setup():
#     driver = webdriver.Chrome(service=browser)
#     return driver

@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        driver = webdriver.Chrome(service=Service("./drivers/chromedriver.exe"))
        print("launching Chrome browser")
    elif browser == "firefox":
        driver = webdriver.Firefox(service=Service("./drivers/geckodriver.exe"))
        print("launching FireFox browser")
    else:
        driver = webdriver.Chrome(service=Service("./drivers/chromedriver.exe"))
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


# to generate html report
def pytest_configure(config):
    config._metadata['Project Name'] = 'E-commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Santosh Sharma'
   

@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)

