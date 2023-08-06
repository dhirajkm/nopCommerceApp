import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class AddCustomer:
    # Add customer page
    lnkCustomers_menu_xpath = "//a/i[@class='nav-icon far fa-user']"
    lnkCustomers_menuitem_xpath = "//a/p[text()=' Customers']"
    btnAddnew_xpath = "//a[@class='btn btn-primary']"
    txtEmail_xpath = "//input[@id='Email']"
    txtPassword_xpath = "//input[@id='Password']"
    txtFirstName_xpath = "//input[@id='FirstName']"
    txtLastName_xpath = "//input[@id='LastName']"
    rdMaleGender_id = "Gender_Male"
    rdFemaleGender_id = "Gender_Female"
    txtDob_xpath = "//input[@id='DateOfBirth']"
    txtCompanyName_xpath = "//input[@id='Company']"
    txtNewsletter_xpath = "//ul[@id='SelectedNewsletterSubscriptionStoreIds_taglist']"
    lstYourStoreName_xpath = "//span[contains(text(), 'Your store name')]"
    lstTestStore2_xpath = "//span[contains(text(), 'Test store 2')]"
    txtCustomerRoles_xpath = "//ul[@id='SelectedCustomerRoleIds_taglist']"
    lstRoleRegistered_xpath = "//span[contains(text(),'Registered')]"
    lstRoleAdministrator_xpath = "//span[contains(text(),'Administrators')]"
    lstRoleModerator_xpath = "//span[contains(text(),'Forum Moderators')]"
    lstRoleGuests_xpath = " //span[contains(text(), 'Guests')]"
    lstRoleVendors_xpath = " //span[contains(text(), 'Vendors')]"
    drpmgrofVendor_xpath = "//select[@id='VendorId']"
    txtAdminContent_xpath = "//textarea[@id='AdminComment']"
    btnSave_xpath = "//button[@name='save']"

    def __init__(self,driver):
        self.driver = driver

    def clickonCustomersMenu(self):
        self.driver.find_element(By.XPATH,self.lnkCustomers_menu_xpath).click()

    def clickonCustomersItem(self):
        self.driver.find_element(By.XPATH,self.lnkCustomers_menuitem_xpath).click()

    def clickonAddNew(self):
        self.driver.find_element(By.XPATH,self.btnAddnew_xpath).click()

    def setEmail(self, email):
        self.driver.find_element(By.XPATH,self.txtEmail_xpath).send_keys(email)

    def setPassword(self, password):
        self.driver.find_element(By.XPATH,self.txtPassword_xpath).send_keys(password)

    def setFirstName(self,fName):
        self.driver.find_element(By.XPATH,self.txtFirstName_xpath).send_keys(fName)

    def setLastName(self, lName):
        self.driver.find_element(By.XPATH,self.txtLastName_xpath).send_keys(lName)

    def setGender(self, gender):
        if gender == 'Male':
            self.driver.find_element(By.ID,self.rdMaleGender_id).click()
        elif gender == 'Female':
            self.driver.find_element(By.ID,self.rdFemaleGender_id).click()
        else:
            self.driver.find_element(By.ID,self.rdFemaleGender_id).click()

    def setDob(self, dob):
        self.driver.find_element(By.XPATH,self.txtDob_xpath).send_keys(dob)

    def setCompanyName(self, cName):
        self.driver.find_element(By.XPATH,self.txtCompanyName_xpath).send_keys(cName)

    def setCustomerRoles(self,role):
        self.driver.find_element(By.XPATH,self.txtCustomerRoles_xpath).click()
        time.sleep(3)
        if role == 'Registered':
            self.listItem = self.driver.find_element(By.XPATH,self.lstRoleRegistered_xpath)
        elif role == 'Administrators':
            self.listItem = self.driver.find_element(By.XPATH,self.lstRoleAdministrator_xpath)
        elif role == 'Guests':
            time.sleep(3)
            self.driver.find_element(By.XPATH,"//ul[@id='SelectedCustomerRoleIds_taglist']/li/span[2]").click()
            self.listItem = self.driver.find_element(By.XPATH,self.lstRoleGuests_xpath)
        elif role == 'Forum Moderators':
            self.listItem = self.driver.find_element(By.XPATH,self.lstRoleModerator_xpath)
        elif role=='Vendors':
            self.listItem = self.driver.find_element(By.XPATH,self.lstRoleVendors_xpath)
        else:
            self.listItem = self.driver.find_element(By.XPATH,self.lstRoleGuests_xpath)
        time.sleep(3)
        self.driver.execute_script("arguments[0].click();", self.listItem)

    def setManagerofVendor(self, value):
        dropList = Select(self.driver.find_element(By.XPATH,self.drpmgrofVendor_xpath))
        dropList.select_by_visible_text(value)

    def setAdminComment(self, comment):
        self.driver.find_element(By.XPATH,self.txtAdminContent_xpath).send_keys(comment)

    def clickSave(self):
        self.driver.find_element(By.XPATH,self.btnSave_xpath).click()