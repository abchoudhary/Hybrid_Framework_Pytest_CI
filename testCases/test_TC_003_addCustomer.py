import pytest
from pageObjects.LoginPage import LoginPage
from pageObjects.AddCustomerPage import AddCustomerPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGeneration
import random
import string
import time


class Test003AddCustomer:
    baseURL = ReadConfig.get_application_url()
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()

    logger = LogGeneration.log_generation()

    @pytest.mark.sanity
    def test_add_customer(self, setup):
        self.logger.info("************* Test_003_AddCustomer *************")
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.baseURL)

        # Creating an object of Login Page class
        self.login_page = LoginPage(self.driver)
        self.login_page.set_username(self.username)
        self.login_page.set_password(self.password)
        self.login_page.click_login()
        self.logger.info("Login successful")

        self.logger.info("Starting add customer test")
        # Creating an object of Add Customer Page class
        self.add_customer_page = AddCustomerPage(self.driver)
        self.add_customer_page.click_customer_menu()
        time.sleep(2)
        self.add_customer_page.click_customer()
        self.add_customer_page.click_add_new()

        self.logger.info("Entering new customer information")
        self.email = random_generator() + '@gmail.com'
        self.add_customer_page.set_email(self.email)
        self.add_customer_page.set_password('test123')
        self.add_customer_page.set_first_name('John')
        self.add_customer_page.set_last_name('Doe')
        self.add_customer_page.set_gender('Male')
        self.add_customer_page.set_dob('11/11/1996')
        self.add_customer_page.set_company('busyQA')
        self.add_customer_page.set_tax_exempt()
        self.add_customer_page.set_newsletter('Test store 2')
        self.add_customer_page.set_customer_roles('Vendors')
        self.add_customer_page.set_manager_of_vendor('Vendor 1')
        self.add_customer_page.set_active()
        self.add_customer_page.set_admin_comment('This is a new customer for testing purpose')
        self.add_customer_page.click_save()

        self.logger.info("Saving new customer information")
        self.logger.info("Add customer validation started")

        self.success_msg = self.driver.find_element_by_tag_name('body').text
        if 'customer has been added successfully' in self.success_msg:
            assert True
            self.logger.info("Add customer test passed")
        else:
            self.driver.save_screenshot("./Screenshots/test_add_customer.png")
            self.logger.error("Add customer test case failed")
            assert False


def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
