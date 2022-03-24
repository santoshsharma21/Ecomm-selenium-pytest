# import lib
import pytest
from pageObjects.LoginPage import LoginPage
from pageObjects.SearchCustomerPage import SerachCustomer
from pageObjects.AddCustomerPage import AddCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_04_serach_customer_by_mail:
    url = ReadConfig.get_url()
    admin_mail = ReadConfig.get_user_email()
    admin_password = ReadConfig.get_password()
    logger = LogGen.loggen()
    
    @pytest.mark.regression
    def test_searchCustomer_by_mail(self, setup):
        self.logger.info("***** Test_004_Search_Customer_by_mail *****")
        self.driver = setup 
        self.driver.get(self.url)
        
        # login 
        login = LoginPage(self.driver)
        login.input_user_email(self.admin_mail)
        login.input_password(self.admin_password)
        login.click_login_btn()
        self.logger.info("*** login sucessful ***")
        
        # select customer menu
        cst_menu = AddCustomer(self.driver)
        cst_menu.select_customer_menu()
        cst_menu.click_customer_submenu()
        
        # search customer by e-mail id
        self.logger.info("*** Searching customer using mail-id ***")
        srch_cst = SerachCustomer(self.driver)
        srch_cst.input_cst_email('victoria_victoria@nopCommerce.com')
        srch_cst.click_search_btn()

        # verify the result
        status = srch_cst.search_cst_by_mail("victoria_victoria@nopCommerce.com")
        self.driver.close()
        if status == True:
            assert True
            self.logger.info("*** Seraching customer by mail test sucessful")
        else:
            self.logger.info("*** Seraching customer by mail test failed ***")
            assert False


