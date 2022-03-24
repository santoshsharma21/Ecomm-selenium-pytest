# import package and modules
import time
import pytest
from utilities import XLUtils
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig
from pageObjects.LoginPage import LoginPage

class Test_02_ddt_login:
    url = ReadConfig.get_url()
    file_path = "./testData/LoginData.xlsx"
    logger = LogGen.loggen()
    
    @pytest.mark.regression
    def test_login_ddt(self, setup):
        self.logger.info("**** Test_02_ddt_login ****")
        self.logger.info("**** Starting Login ddt test ****")
        self.driver = setup
        self.driver.get(self.url)

        self.login = LoginPage(self.driver)

        # get rowcount from excel file
        total_rows = XLUtils.getRowsCount(self.file_path, "Sheet1")
        # initialize empty list to store result
        result = []

        # read data from file
        for row in range(2, total_rows + 1):
            user_email = XLUtils.ReadData(self.file_path, "Sheet1", row, 1)
            user_password = XLUtils.ReadData(self.file_path, "Sheet1", row, 2)
            exp_result = XLUtils.ReadData(self.file_path, "Sheet1", row, 3)

            self.login.input_user_email(user_email)
            self.login.input_password(user_password)
            self.login.click_login_btn()
            time.sleep(5)

            # get the title of the loged in page
            page_title = self.driver.title
            exp_page_title = "Dashboard / nopCommerce administration"

            # verify the output
            if page_title == exp_page_title:
                if exp_result == 'Pass':
                    result.append("Pass")
                    self.logger.info("*** Passed ***")
                    self.login.click_logout()
                elif exp_result == "Fail":
                    result.append("Fail")
                    self.logger.error("*** Failed ***")
                    self.login.click_logout()
            
            elif page_title != exp_page_title:
                if exp_result == 'Pass':
                    result.append("Fail")
                    self.logger.error("*** Failed ***")
                elif exp_result == "Fail":
                    result.append("Pass")
                    self.logger.info("*** Passed ***")

        if "Fail" not in result:
            self.logger.info("*** DDT Login Test Passed")
            self.driver.close()
            assert True 
        else:
            self.logger.error("*** DDT Login Test Failed ***")
            self.driver.close()
            assert False 

        self.logger.info("***** Completed  Test_02_ddt_login completed *****")
        print(result)
