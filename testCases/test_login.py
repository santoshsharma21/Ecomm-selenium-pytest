# import lib
import pytest
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_01_Login:
    url = ReadConfig.get_url()
    user_email = ReadConfig.get_user_email()
    password = ReadConfig.get_password()
    log = LogGen.loggen()
    
    @pytest.mark.regression
    def test_homepage_title(self, setup):
        self.log.info("** Test_001_Login **")
        self.log.info("** Verifying Home Page **")
        self.driver = setup
        self.driver.get(self.url)
        page_title = self.driver.title

        if page_title == "Your store. Login":
            assert True
            self.driver.close()
            self.log.info("Home page title verified")
        else:
            self.driver.save_screenshot("./screenshots/homepage_title_failed.png")
            self.driver.close()
            self.log.error("Home page title test failed")
            assert False
    
    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login_page(self, setup):
        self.log.info("** Verifying Login test **")
        self.driver = setup
        self.driver.get(self.url)
        
        self.login = LoginPage(self.driver)
        self.login.input_user_email(self.user_email)
        self.login.input_password(self.password)
        self.login.click_login_btn()
        page_title = self.driver.title
        # self.login.click_logout()

        if page_title == "Dashboard / nopCommerce administration":
            assert True
            self.log.info("Login test passed")
            self.driver.close()
        else:
            self.driver.save_screenshot("./screenshots/login_page_failed.png")
            self.driver.close()
            self.log.error("Login test failed")
            assert False
