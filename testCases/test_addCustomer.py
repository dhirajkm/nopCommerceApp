import random
import string
import pytest
from selenium.webdriver.common.by import By

from pageObjects.AddCustomerPage import AddCustomer
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_AddCustomer_003:
    baseUrl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getUserpassword()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_addCustomer(self, setup):
        self.logger.info("###########Test_003_AddCustomer################")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("############Login Successful#############")

        self.logger.info("#############starting Add New CUstomer Test##################")
        self.addCust = AddCustomer(self.driver)
        self.addCust.clickonCustomersMenu()
        self.addCust.clickonCustomersItem()
        self.addCust.clickonAddNew()

        self.logger.info("############Providing customer info###############")
        self.email = random_generator()+"@gmail.com"
        self.addCust.setEmail(self.email)
        self.addCust.setPassword("test123")
        self.addCust.setFirstName("Dhiraj")
        self.addCust.setLastName("Maharjan")
        self.addCust.setGender("Male")
        self.addCust.setDob("04/15/1982")
        self.addCust.setCompanyName("SharkNinja")
        self.addCust.setCustomerRoles("Administrator")
        self.addCust.setManagerofVendor("Vendor 2")
        self.addCust.setAdminComment("User information collected for testing$$$$$$$$$$$$$$$$$$")
        self.addCust.clickSave()

        self.logger.info("##################saving customer info################")

        self.logger.info("#############Add Customer validation started####################")
        self.message = self.driver.find_element(By.TAG_NAME,"body").text
        print(self.message)

        if 'The new customer has been added successfully.' in self.message:
            assert True == True
            self.logger.info("################Add Customer Test passed###################")
        else:
            self.driver.save_screenshot(".\\screenshots" + "test_addCustomer_scr.png")
            self.logger.error("################Add Customer Test failed##############")
            assert True == False
        self.driver.implicitly_wait(5)
        self.driver.close()
        self.logger.info("###################Ending Add Customer Test##############")

def random_generator(size=12, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))