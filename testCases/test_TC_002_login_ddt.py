import pytest
import time
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGeneration
from utilities import excelUtils


class Test002DataDrivenLogin:
    baseURL = ReadConfig.get_application_url()
    path = ".//TestData/login_test_data.xlsx"

    logger = LogGeneration.log_generation()

    @pytest.mark.regression
    def test_login_ddt(self, setup):
        self.logger.info("************* Test_002_DDT_Login *************")
        self.logger.info("*** Verifying Login DDT test ***")
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.baseURL)

        # Creating object of LoginPage class
        self.login_page = LoginPage(self.driver)

        self.rows = excelUtils.get_row_count(self.path, 'Sheet1')
        self.cols = excelUtils.get_col_count(self.path, 'Sheet1')

        status_list = []

        for row in range(2, self.rows+1):
            self.username = excelUtils.read_data(self.path, 'Sheet1', row, 1)
            self.password = excelUtils.read_data(self.path, 'Sheet1', row, 2)
            self.expected = excelUtils.read_data(self.path, 'Sheet1', row, 3)

            self.login_page.set_username(self.username)
            self.login_page.set_password(self.password)
            self.login_page.click_login()
            time.sleep(2)

            actual_title = self.driver.title
            expected_title = "Dashboard / nopCommerce administration"

            if actual_title == expected_title:
                if self.expected == "Pass":
                    self.logger.info("Scenario passed")
                    self.login_page.click_logout()
                    status_list.append("Pass")
                elif self.expected == "Fail":
                    self.logger.info("Scenario failed")
                    self.login_page.click_logout()
                    status_list.append("Fail")

            elif actual_title != expected_title:
                if self.expected == "Pass":
                    self.logger.info("Scenario failed")
                    status_list.append("Fail")
                elif self.expected == "Fail":
                    self.logger.info("Scenario passed")
                    status_list.append("Pass")

        if "Fail" not in status_list:
            self.logger.info("Data driven login test passed")
            self.driver.close()
            assert True
        else:
            self.logger.info("Data driven login test failed")
            self.driver.close()
            assert False

        self.logger.info("*** End of Login DDT test ***")
