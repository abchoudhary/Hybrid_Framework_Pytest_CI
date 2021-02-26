import pytest
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGeneration


class Test001Login:
    baseURL = ReadConfig.get_application_url()
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()

    logger = LogGeneration.log_generation()

    @pytest.mark.regression
    def test_homepage_title(self, setup):
        self.logger.info("************* Test_001_Login *************")
        self.logger.info("*** Started home page title test ***")
        self.driver = setup
        self.driver.maximize_window()
        self.logger.info("Opening application URL")
        self.driver.get(self.baseURL)
        actual_title = self.driver.title
        if actual_title == "Your store. Login":
            self.logger.info("Home page title test is passed")
            assert True
        else:
            self.logger.error("Home page title test is failed")
            self.driver.save_screenshot("./Screenshots/test_homepage_title.png")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self, setup):
        self.logger.info("*** Started login test ***")
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.baseURL)

        # Creating an object of LoginPage class
        self.login_page = LoginPage(self.driver)
        self.login_page.set_username(self.username)
        self.login_page.set_password(self.password)
        self.login_page.click_login()
        actual_title = self.driver.title
        if actual_title == "Dashboard / nopCommerce administration":
            self.logger.info("Login test is passed")
            assert True
        else:
            self.logger.error("Login test is failed")
            self.driver.save_screenshot("./Screenshots/test_login.png")
            assert False
