from selenium.webdriver.support.ui import Select
from Resources.Locators_AddCustomer import AddCustomerLocators
import time


class AddCustomerPage:
    def __init__(self, driver):
        self.driver = driver

    def click_customer_menu(self):
        self.driver.find_element(*AddCustomerLocators.CUSTOMER_MENU_LINK).click()

    def click_customer(self):
        self.driver.find_element(*AddCustomerLocators.CUSTOMER_ITEM_LINK).click()

    def click_add_new(self):
        self.driver.find_element(*AddCustomerLocators.ADD_NEW_BUTTON).click()

    def set_email(self, email):
        self.driver.find_element(*AddCustomerLocators.EMAIL_TEXTBOX).clear()
        self.driver.find_element(*AddCustomerLocators.EMAIL_TEXTBOX).send_keys(email)

    def set_password(self, password):
        self.driver.find_element(*AddCustomerLocators.PASSWORD_TEXTBOX).clear()
        self.driver.find_element(*AddCustomerLocators.PASSWORD_TEXTBOX).send_keys(password)

    def set_first_name(self, first_name):
        self.driver.find_element(*AddCustomerLocators.FIRSTNAME_TEXTBOX).clear()
        self.driver.find_element(*AddCustomerLocators.FIRSTNAME_TEXTBOX).send_keys(first_name)

    def set_last_name(self, last_name):
        self.driver.find_element(*AddCustomerLocators.LASTNAME_TEXTBOX).clear()
        self.driver.find_element(*AddCustomerLocators.LASTNAME_TEXTBOX).send_keys(last_name)

    def set_gender(self, gender):
        if gender == 'Male':
            self.driver.find_element(*AddCustomerLocators.GENDER_MALE_RADIO).click()
        elif gender == 'Female':
            self.driver.find_element(*AddCustomerLocators.GENDER_FEMALE_RADIO).click()
        else:
            self.driver.find_element(*AddCustomerLocators.GENDER_MALE_RADIO).click()

    def set_dob(self, dob):
        self.driver.find_element(*AddCustomerLocators.DOB_TEXTBOX).clear()
        self.driver.find_element(*AddCustomerLocators.DOB_TEXTBOX).send_keys(dob)

    def set_company(self, company):
        self.driver.find_element(*AddCustomerLocators.COMPANY_TEXTBOX).clear()
        self.driver.find_element(*AddCustomerLocators.COMPANY_TEXTBOX).send_keys(company)

    def set_tax_exempt(self):
        element = self.driver.find_element(*AddCustomerLocators.TAX_CHECKBOX)
        if not element.is_selected():
            element.click()

    def set_newsletter(self, newsletter):
        self.driver.find_element(*AddCustomerLocators.NEWSLETTER_TEXTBOX).click()
        time.sleep(2)
        if newsletter == "Your store name":
            self.newsItem = self.driver.find_element(*AddCustomerLocators.YOUR_STORE_LIST_ITEM)
        else:
            self.newsItem = self.driver.find_element(*AddCustomerLocators.TEST_STORE2_LIST_ITEM)
        time.sleep(2)
        self.driver.execute_script("arguments[0].click();", self.newsItem)

    def set_customer_roles(self, role):
        self.driver.find_element(*AddCustomerLocators.CUSTOMER_ROLES_TEXTBOX).click()
        time.sleep(3)
        if role == "Registered":
            self.listItem = self.driver.find_element(*AddCustomerLocators.REGISTERED_LIST_ITEM)
        elif role == "Administrators":
            self.listItem = self.driver.find_element(*AddCustomerLocators.ADMINISTRATORS_LIST_ITEM)
        elif role == "Guests":
            # Here user can be either Registered or Guests
            time.sleep(2)
            self.driver.find_element_by_xpath("//*[@id='SelectedCustomerRoleIds_taglist']//li[2]//span[2]").click()
            self.listItem = self.driver.find_element(*AddCustomerLocators.GUESTS_LIST_ITEM)
        elif role == 'Registered':
            self.listItem = self.driver.find_element(*AddCustomerLocators.REGISTERED_LIST_ITEM)
        elif role == 'Vendors':
            self.listItem = self.driver.find_element(*AddCustomerLocators.VENDORS_LIST_ITEM)
        else:
            self.listItem = self.driver.find_element(*AddCustomerLocators.GUESTS_LIST_ITEM)
        time.sleep(2)
        self.driver.execute_script("arguments[0].click();", self.listItem)

    def set_manager_of_vendor(self, value):
        drp = Select(self.driver.find_element(*AddCustomerLocators.VENDOR_DROPDOWN))
        drp.select_by_visible_text(value)

    def set_active(self):
        element = self.driver.find_element(*AddCustomerLocators.ACTIVE_CHECKBOX)
        if not element.is_selected():
            element.click()

    def set_admin_comment(self, comments):
        self.driver.find_element(*AddCustomerLocators.ADMIN_TEXTAREA).clear()
        self.driver.find_element(*AddCustomerLocators.ADMIN_TEXTAREA).send_keys(comments)

    def click_save(self):
        self.driver.find_element(*AddCustomerLocators.SAVE_BUTTON).click()
