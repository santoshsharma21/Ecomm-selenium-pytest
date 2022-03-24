# import libraries
from selenium.webdriver.common.by import By

#class
class SerachCustomer:
    textbox_SearchEmail_id = "SearchEmail"
    textbox_SearchFirstName_id = "SearchFirstName"
    textbox_SearchLastName_id = "SearchLastName"
    btn_Search_id = "search-customers"
    table_xpath = "//table[@id='customers-grid']"
    table_rows_xpath = "//table[@id='customers-grid']//tbody/tr"
    table_cols_xpath = "//table[@id='customers-grid']//tbody/tr/td"

    def __init__(self, driver):
        self.driver = driver

    def input_cst_email(self, cst_email):
        self.driver.find_element(By.ID, self.textbox_SearchEmail_id).clear()
        self.driver.find_element(By.ID, self.textbox_SearchEmail_id).send_keys(cst_email)

    def input_first_name(self, fname):
        self.driver.find_element(By.ID, self.textbox_SearchFirstName_id).clear()
        self.driver.find_element(By.ID, self.textbox_SearchFirstName_id).send_keys(fname)

    def input_last_name(self, lname):
        self.driver.find_element(By.ID, self.textbox_SearchLastName_id).clear()
        self.driver.find_element(By.ID, self.textbox_SearchLastName_id).send_keys(lname)

    def click_search_btn(self):
        self.driver.find_element(By.ID, self.btn_Search_id).click()

    def get_nrows(self):
        return len(self.driver.find_elements(By.XPATH, self.table_rows_xpath))

    def get_ncols(self):
        return len(self.driver.find_elements(By.XPATH, self.table_cols_xpath))
        

    def search_cst_by_mail(self, mail):
        flag = False
        for i in range(1, self.get_nrows() + 1):
            table = self.driver.find_element(By.XPATH, self.table_xpath)
            cst_email = table.find_element(By.XPATH,"//table[@id='customers-grid']//tbody/tr["+str(i)+"]/td[2]").text
            if mail == cst_email:
                flag = True
                break
        return flag

    def search_cst_by_name(self, name):
        flag = False
        for i in range(1, self.get_ncols() + 1):
            table = self.driver.find_element(By.XPATH, self.table_xpath)
            cst_name = table.find_element(By.XPATH,"//table[@id='customers-grid']//tbody/tr["+str(i)+"]/td[3]").text
            if name == cst_name:
                flag = True
                break
        return flag




