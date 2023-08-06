import time
import pytest

from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import xlUtils

class Test_Login_DDT_002:
    baseUrl = ReadConfig.getApplicationURL()
    path = ".//testData/loginData.xlsx"
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_login_ddt(self,setUp):
        self.logger.info("*********Test_002_Login_DDT**********")
        self.logger.info("$$$$$verifying login DDT test$$$$$$$$")
        self.driver = setUp
        self.driver.get(self.baseUrl)

        self.lp = LoginPage(self.driver)
        self.rows = xlUtils.getRowCount(self.path, 'sheet1')
        print("Number of rows", self.rows)

        lst_status = [] # Empty list variable

        for r in range (2, self.rows+1):
            self.user = xlUtils.readData(self.path, 'sheet1', r, 1)
            self.password = xlUtils.readData(self.path, 'sheet1', r,2)
            self.expected = xlUtils.readData(self.password, 'sheet1', r, 3)

            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)

            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            if act_title == exp_title:
                if self.expected=="pass":
                    self.logger.info("passed")
                    self.lp.clickLogout()
                    lst_status.append("pass")

                elif self.expected=="fail":
                    self.logger.info("failed")
                    self.lp.clickLogout()
                    lst_status.append("fail")

            elif act_title != exp_title:
                if self.expected=="fail":
                    self.logger.info("failed")
                    self.lp.clickLogout()
                    lst_status.append("fail")

                elif self.expected=="pass":
                    self.logger.info("passed")
                    self.lp.clickLogout()
                    lst_status.append("pass")

        if "fail" not in lst_status:
            self.logger.info("Login DDT test passsed")
            self.driver.close()
            assert True

        else:
            self.logger.info("Login DDT test failed")
            self.driver.close()
            assert False

        self.logger.info("End of login DDT test")
        self.logger.info("compteted test_Login_002_ddt ")

