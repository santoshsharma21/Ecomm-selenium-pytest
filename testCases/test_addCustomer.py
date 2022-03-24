# import required lib and custom modules
import pytest
import time
import string
import random 
from selenium.webdriver.common.by import By
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig
from pageObjects.LoginPage import LoginPage
from pageObjects.AddCustomerPage import AddCustomer

# func to generate random data
def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))


# test class
class Test_03_AddCustomer:
    url = ReadConfig.get_url()
    admin_email = ReadConfig.get_user_email()
    admin_password = ReadConfig.get_password()
    logger = LogGen.loggen()
    
    @pytest.mark.sanity
    @pytest.mark.regression
    def test_add_customer(self, setup):
        self.logger.info("***** Test_003_AddCustomer *****")
        self.driver = setup
        self.driver.get(self.url)
        
        # Admin login
        login = LoginPage(self.driver)
        login.input_user_email(self.admin_email)
        login.input_password(self.admin_password)
        login.click_login_btn()
        self.logger.info("*** Login Succesful ***")

        # add new customer
        self.logger.info("*** Starting Add customer Test ***")
        add_cst = AddCustomer(self.driver)
        add_cst.select_customer_menu()
        add_cst.click_customer_submenu()
        add_cst.click_add_new()
        id = random_generator()+'@gmail.com'
        add_cst.input_email(id)
        add_cst.input_password('hello')
        add_cst.input_first_name('Santosh')
        add_cst.input_last_name('Sharma')
        add_cst.select_gender('Male')
        add_cst.input_dob('2/21/2020')
        add_cst.input_company_name('TCS')
        add_cst.click_is_tax()
        add_cst.select_customer_roles('Guest')
        add_cst.select_manager_vendor('Vendor 1')
        #add_cst.click_active()
        add_cst.input_comment('This is for testing')
        add_cst.click_save()
        self.logger.info("*** Saved customer info ***")

        msg = self.driver.find_element(By.TAG_NAME, "body").text
        
        # validate
        if 'customer has been added successfully.' in msg:
            assert True
            self.logger.info("*** Add Customer Test Passed ***")
        else:
            self.driver.save_screenshot('./screenshots/add_customer.png')
            self.logger.info("*** Add customer test Failed ***")
            assert False 
        
        # close driver
        self.driver.close()