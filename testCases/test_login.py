import pytest
import time
from pageObjects.LoginPage import LoginPage
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig

class Test_Login_001:
    baseUrl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getUserpassword()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_homepage_title(self, setup):
        self.logger.info("$$$$$$$$$Test_Login_001$$$$$$$$$$")
        self.logger.info("verifying home title")
        self.driver = setup
        self.driver.implicitly_wait(10)
        self.driver.get(self.baseUrl)
        actual_title = self.driver.title
        if actual_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("home page title test is passed")
        else:
            self.driver.save_screenshot(".\\screenshots\\"+"test_homepage_title.png")
            self.driver.close()
            self.logger.error("home page title lpage is failed")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self,setup):
        self.logger.info("$$$$$verifying login test$$$$$$$$")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        actual_title = self.driver.title
        self.driver.close()
        if actual_title == "Dashboard / nopCommerce administration":
            assert True
            self.logger.info("################Login test is passed#################")
            self.driver.close()

        else:
            self.driver.save_screenshot(".\\screenshots\\"+"test_login.png")
            self.driver.close()
            self.logger.error("####################Login test is failed###################")
            assert False

