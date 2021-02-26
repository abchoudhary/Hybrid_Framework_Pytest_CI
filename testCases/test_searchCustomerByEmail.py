import pytest
from pageObjects.LoginPage import LoginPage
from pageObjects.AddCustomerPage import AddCustomerPage
from pageObjects.SearchCustomer import SearchCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGeneration
import time


class Test004SearchCustomerByEmail:
    baseURL = ReadConfig.get_application_url()
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()

    logger = LogGeneration.log_generation()

    @pytest.mark.regression
    def test_search_customer_by_email(self, setup):
        self.logger.info("************* Test_004_SearchCustomerByEmail *************")
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.baseURL)

        self.logger.info("Entering login credentials")
        self.login_page = LoginPage(self.driver)
        self.login_page.set_username(self.username)
        self.login_page.set_password(self.password)
        self.login_page.click_login()
        self.logger.info("Login successful")

        self.logger.info("Clicking on customer menu")
        self.customer_page = AddCustomerPage(self.driver)
        self.customer_page.click_customer_menu()
        time.sleep(2)
        self.customer_page.click_customer()

        self.logger.info("Searching customer by email")
        self.search_customer = SearchCustomer(self.driver)
        self.search_customer.set_search_email('admin@yourStore.com')
        self.search_customer.click_search()
        time.sleep(3)
        status = self.search_customer.search_customer_by_email('admin@yourStore.com')
        assert True == status
        self.logger.info("Test_004_SearchCustomerByEmail finished")
        self.driver.close()
