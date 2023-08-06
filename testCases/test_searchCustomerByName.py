import time
import pytest

from pageObjects.SearchCustomerPage import SearchCustomer
from pageObjects.AddCustomerPage import AddCustomer
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_SearchCustomerByName_005:
    baseUrl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getUserpassword()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_searchCustomerByName(self, setup):
        self.logger.info("#############SearchCustomerByName_005##################")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("$$$$$$$$$$$$$Login Successful$$$$$$$$$$$$$$$$$$")

        self.logger.info("#################Starting search customer by Name###################")

        self.addCust = AddCustomer(self.driver)
        self.addCust.clickonCustomersMenu()
        self.addCust.clickonCustomersItem()

        self.logger.info("###############Searching customer by Name#####################")
        self.searchCust = SearchCustomer(self.driver)
        self.searchCust.setFirstName("victoria")
        self.searchCust.setLastName("Terces")
        self.searchCust.clickSearch()
        time.sleep(5)
        status = self.searchCust.seacrhCustomerByName("Victoria Terces")
        assert True == status
        self.logger.info("$$$$$$$$$$$$$$$$Search customer by Name is complete$$$$$$$$$$$$$$$$$$$")
        self.driver.close()