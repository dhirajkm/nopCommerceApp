import pytest
from selenium import webdriver
from pytest_metadata import plugin

@pytest.fixture()
def setup(browser):
   if browser == "chrome":
        # driver = webdriver.Chrome()
        from selenium.webdriver.chrome.service import Service
        observ = Service()
        driver=webdriver.Chrome(service=observ)
        print("*******Launching Chrome browser*******")
        driver.implicitly_wait(5)
   elif browser == "firefox":
        # driver = webdriver.Firefox()
        from selenium.webdriver.firefox.service import Service
        observ = Service()
        driver=webdriver.Firefox(service=observ)
        print("*******Launching Firefox browser*******")
        driver.implicitly_wait(5)
   else:
        # driver = webdriver.Edge()
        from selenium.webdriver.edge.service import Service
        observ = Service()
        driver=webdriver.Edge(service=observ)
        print("*******Launching Edge browser*******")
        driver.implicitly_wait(5)
   return driver


def pytest_addoption(parser): #This will get the values from the CLI/hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

#########Pytest Html reports#######

# It is a hook for adding environment into the html report

# def pytest_configure(config):
#     config._metadata['Project_Name'] = 'nop Commerce'
#     config._metadata['Module_Name'] = 'Customers'
#     config._metadata['Tester'] = 'Dhiraj'

# It is a hook for deleting/modifying environment into the html report

# @pytest.mark.optionalhook
@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("Java_Home", None)
    metadata.pop("Plugins", None)
