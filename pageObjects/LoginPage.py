from Resources.Locators_LoginPage import LoginPageLocators


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def set_username(self, username):
        self.driver.find_element(*LoginPageLocators.USERNAME_TEXTBOX).clear()
        self.driver.find_element(*LoginPageLocators.USERNAME_TEXTBOX).send_keys(username)

    def set_password(self, password):
        self.driver.find_element(*LoginPageLocators.PASSWORD_TEXTBOX).clear()
        self.driver.find_element(*LoginPageLocators.PASSWORD_TEXTBOX).send_keys(password)

    def click_login(self):
        self.driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

    def click_logout(self):
        self.driver.find_element(*LoginPageLocators.LOGOUT_LINK).click()
