# import required libraries and modules
import time 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

# Page object
class AddCustomer:
    link_Customers_menu_xpath = "//body[1]/div[3]/aside[1]/div[1]/div[4]/div[1]/div[1]/nav[1]/ul[1]/li[4]/a[1]/p[1]" 
    link_Customers_menuItem_xpath = "//body[1]/div[3]/aside[1]/div[1]/div[4]/div[1]/div[1]/nav[1]/ul[1]/li[4]/ul[1]/li[1]/a[1]/p[1]"     
    btn_AddNew_xpath = "//a[@href='/Admin/Customer/Create']"
    textbox_Email_id = "Email"
    textbox_Password_id = "Password"
    textbox_FirstName_id = "FirstName"
    textbox_LastName_id = "LastName"
    radiobtn_Gender_male_id = "Gender_Male"
    radiobtn_Gender_female_id = "Gender_Female"
    text_Dob_id = "DateOfBirth"
    textbox_CompanyName_id = "Company"
    checkbox_IsTax_exempt_id = "IsTaxExempt" 
    listbox_CustomerRoles_xpath = "//div[@class='k-multiselect-wrap k-floatwrap']"
    CstRoleItem_Administartor_xpath = "//li[contains(text(),'Administrators')]"
    CstRoleItem_ForumModerators_xpath = "//li[contains(text(),'Forum Moderators')]"
    CstRoleItem_Guest_xpath = "//li[contains(text(),'Guests')]"
    CstRoleItem_Registered_xpath = "//li[contains(text(),'Registered')]"
    CstRoleItem_Vendor_xpath = "//li[contains(text(),'Vendors')]"
    dropdwn_ManagerVendor_id = "VendorId"                                       
    checkbox_Active_id = "Active"
    textbox_AdminContent_id = "AdminComment"
    btn_Save_xpath = "//button[@name='save']"

    def __init__(self, driver):
        self.driver = driver

    def select_customer_menu(self):
        self.driver.find_element(By.XPATH, self.link_Customers_menu_xpath).click()

    def click_customer_submenu(self):
        self.driver.find_element(By.XPATH, self.link_Customers_menuItem_xpath).click()

    def click_add_new(self):
        self.driver.find_element(By.XPATH, self.btn_AddNew_xpath).click()

    def input_email(self, email_id):
        self.driver.find_element(By.ID, self.textbox_Email_id).clear()
        self.driver.find_element(By.ID, self.textbox_Email_id).send_keys(email_id)

    def input_password(self, password):
        self.driver.find_element(By.ID, self.textbox_Password_id).clear()
        self.driver.find_element(By.ID, self.textbox_Password_id).send_keys(password)

    def input_first_name(self, first_name):
        self.driver.find_element(By.ID, self.textbox_FirstName_id).clear()
        self.driver.find_element(By.ID, self.textbox_FirstName_id).send_keys(first_name)

    def input_last_name(self, last_name):
        self.driver.find_element(By.ID, self.textbox_LastName_id).clear()
        self.driver.find_element(By.ID, self.textbox_LastName_id).send_keys(last_name)

    def select_gender(self, gender):
        if gender == 'Male':
            self.driver.find_element(By.ID, self.radiobtn_Gender_male_id).click()
        elif gender == 'Female':
            self.driver.find_element(By.ID, self.radiobtn_Gender_female_id).click()
        else:
            self.driver.find_element(By.ID, self.radiobtn_Gender_male_id).click()

    def input_dob(self, dob):
        self.driver.find_element(By.ID, self.text_Dob_id).clear()
        self.driver.find_element(By.ID, self.text_Dob_id).send_keys(dob)

    def input_company_name(self, company_name):
        self.driver.find_element(By.ID, self.textbox_CompanyName_id).clear()
        self.driver.find_element(By.ID, self.textbox_CompanyName_id).send_keys(company_name)

    def click_is_tax(self):
        self.driver.find_element(By.ID, self.checkbox_IsTax_exempt_id).click()

    def select_customer_roles(self, role):
        self.driver.find_element(By.XPATH, self.listbox_CustomerRoles_xpath).click()
        time.sleep(3)
        if role == 'Administrators':
            list_item = self.driver.find_element(By.XPATH, self.CstRoleItem_Administartor_xpath)
        elif role == 'Forum Moderators':
            list_item = self.driver.find_element(By.XPATH, self.CstRoleItem_ForumModerators_xpath)
        elif role == 'Guest':
            time.sleep(2)
            self.driver.find_element(By.XPATH, "//*[@id='SelectedCustomerRoleIds_taglist']/li/span[2]").click()
            list_item = self.driver.find_element(By.XPATH, self.CstRoleItem_Guest_xpath)
        elif role == 'Registered':
            list_item = self.driver.find_element(By.XPATH, self.CstRoleItem_Registered_xpath)
        elif role == 'Vendor':
            list_item = self.driver.find_element(By.XPATH, self.CstRoleItem_Vendor_xpath)
        
        time.sleep(2)
        self.driver.execute_script("arguments[0].click();", list_item)


    def select_manager_vendor(self, vendor):
        drp_dwn = Select(self.driver.find_element(By.ID, self.dropdwn_ManagerVendor_id))
        drp_dwn.select_by_visible_text(vendor)

    def click_active(self):
        self.driver.find_element(By.ID, self.checkbox_Active_id).click()

    def input_comment(self, comment):
        self.driver.find_element(By.ID, self.textbox_AdminContent_id).clear()
        self.driver.find_element(By.ID, self.textbox_AdminContent_id).send_keys(comment)

    def click_save(self):
        self.driver.find_element(By.XPATH, self.btn_Save_xpath).click()







    