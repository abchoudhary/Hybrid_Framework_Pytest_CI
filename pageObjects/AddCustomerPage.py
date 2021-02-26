from selenium.webdriver.support.ui import Select
import time


class AddCustomerPage:
    link_customer_menu_xpath = "//a[@href='#']//span[contains(text(),'Customers')]"
    link_customer_item_xpath = "//span[@class='menu-item-title'][normalize-space()='Customers']"
    button_add_new_xpath = "//a[normalize-space()='Add new']"

    textbox_email_id = "Email"
    textbox_password_id = "Password"
    textbox_firstname_id = "FirstName"
    textbox_lastname_id = "LastName"
    radio_gender_male_id = "Gender_Male"
    radio_gender_female_id = "Gender_Female"
    textbox_dob_id = "DateOfBirth"
    textbox_company_id = "Company"
    checkbox_tax_id = "IsTaxExempt"

    # Handling textbox with options to choose
    textbox_newsletter_xpath = "(//div[@class='k-multiselect-wrap k-floatwrap'])[1]"
    listItem_yourStore_xpath = "//li[contains(text(), 'Your store name')]"
    listItem_test_store2_xpath = "//li[contains(text(), 'Test store 2')]"

    textbox_customer_roles_xpath = "(//div[@class='k-multiselect-wrap k-floatwrap'])[2]"
    listItem_administrators_xpath = "//li[contains(text(), 'Administrators')]"
    listItem_registered_xpath = "//li[contains(text(), 'Registered')]"
    listItem_guests_xpath = "//li[contains(text(), 'Guests')]"
    listItem_vendors_xpath = "//li[contains(text(), 'Vendors')]"

    dropdown_vendor_id = "VendorId"
    checkbox_active_id = "Active"
    textarea_admin_id = "AdminComment"
    button_save_name = "save"

    def __init__(self, driver):
        self.driver = driver

    def click_customer_menu(self):
        self.driver.find_element_by_xpath(self.link_customer_menu_xpath).click()

    def click_customer(self):
        self.driver.find_element_by_xpath(self.link_customer_item_xpath).click()

    def click_add_new(self):
        self.driver.find_element_by_xpath(self.button_add_new_xpath).click()

    def set_email(self, email):
        self.driver.find_element_by_id(self.textbox_email_id).clear()
        self.driver.find_element_by_id(self.textbox_email_id).send_keys(email)

    def set_password(self, password):
        self.driver.find_element_by_id(self.textbox_password_id).clear()
        self.driver.find_element_by_id(self.textbox_password_id).send_keys(password)

    def set_first_name(self, first_name):
        self.driver.find_element_by_id(self.textbox_firstname_id).clear()
        self.driver.find_element_by_id(self.textbox_firstname_id).send_keys(first_name)

    def set_last_name(self, last_name):
        self.driver.find_element_by_id(self.textbox_lastname_id).clear()
        self.driver.find_element_by_id(self.textbox_lastname_id).send_keys(last_name)

    def set_gender(self, gender):
        if gender == 'Male':
            self.driver.find_element_by_id(self.radio_gender_male_id).click()
        elif gender == 'Female':
            self.driver.find_element_by_id(self.radio_gender_female_id).click()
        else:
            self.driver.find_element_by_id(self.radio_gender_male_id).click()

    def set_dob(self, dob):
        self.driver.find_element_by_id(self.textbox_dob_id).clear()
        self.driver.find_element_by_id(self.textbox_dob_id).send_keys(dob)

    def set_company(self, company):
        self.driver.find_element_by_id(self.textbox_company_id).clear()
        self.driver.find_element_by_id(self.textbox_company_id).send_keys(company)

    def set_tax_exempt(self):
        element = self.driver.find_element_by_id(self.checkbox_tax_id)
        if not element.is_selected():
            element.click()

    def set_newsletter(self, newsletter):
        self.driver.find_element_by_xpath(self.textbox_newsletter_xpath).click()
        time.sleep(2)
        if newsletter == "Your store name":
            self.newsItem = self.driver.find_element_by_xpath(self.listItem_yourStore_xpath)
        else:
            self.newsItem = self.driver.find_element_by_xpath(self.listItem_test_store2_xpath)
        time.sleep(2)
        self.driver.execute_script("arguments[0].click();", self.newsItem)

    def set_customer_roles(self, role):
        self.driver.find_element_by_xpath(self.textbox_customer_roles_xpath).click()
        time.sleep(3)
        if role == "Registered":
            self.listItem = self.driver.find_element_by_xpath(self.listItem_registered_xpath)
        elif role == "Administrators":
            self.listItem = self.driver.find_element_by_xpath(self.listItem_administrators_xpath)
        elif role == "Guests":
            # Here user can be either Registered or Guests
            time.sleep(2)
            self.driver.find_element_by_xpath("//*[@id='SelectedCustomerRoleIds_taglist']//li[2]//span[2]").click()
            self.listItem = self.driver.find_element_by_xpath(self.listItem_guests_xpath)
        elif role == 'Registered':
            self.listItem = self.driver.find_element_by_xpath(self.listItem_registered_xpath)
        elif role == 'Vendors':
            self.listItem = self.driver.find_element_by_xpath(self.listItem_vendors_xpath)
        else:
            self.listItem = self.driver.find_element_by_xpath(self.listItem_guests_xpath)
        time.sleep(2)
        self.driver.execute_script("arguments[0].click();", self.listItem)

    def set_manager_of_vendor(self, value):
        drp = Select(self.driver.find_element_by_id(self.dropdown_vendor_id))
        drp.select_by_visible_text(value)

    def set_active(self):
        element = self.driver.find_element_by_id(self.checkbox_active_id)
        if not element.is_selected():
            element.click()

    def set_admin_comment(self, comments):
        self.driver.find_element_by_id(self.textarea_admin_id).clear()
        self.driver.find_element_by_id(self.textarea_admin_id).send_keys(comments)

    def click_save(self):
        self.driver.find_element_by_name(self.button_save_name).click()
