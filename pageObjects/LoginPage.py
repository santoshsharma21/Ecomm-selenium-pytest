from selenium.webdriver.common.by import By


class LoginPage:
    textbox_user_email_id = "Email"
    textbox_password_id = "Password"
    btn_login_xpath = "//button[contains(text(),'Log in')]"
    link_logout_linktext = "Logout"

    def __init__(self, driver):
        self.driver = driver

    def input_user_email(self, user_email):
        self.driver.find_element(By.ID, self.textbox_user_email_id).clear()
        self.driver.find_element(By.ID, self.textbox_user_email_id).send_keys(user_email)

    def input_password(self, password):
        self.driver.find_element(By.ID, self.textbox_password_id).clear()
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)

    def click_login_btn(self):
        self.driver.find_element(By.XPATH, self.btn_login_xpath).click()

    def click_logout(self):
        self.driver.find_element(By.LINK_TEXT, self.link_logout_linktext).click()
