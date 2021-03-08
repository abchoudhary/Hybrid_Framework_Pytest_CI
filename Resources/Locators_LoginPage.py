from selenium.webdriver.common.by import By


class LoginPageLocators:
    USERNAME_TEXTBOX = (By.ID, "Email")
    PASSWORD_TEXTBOX = (By.ID, "Password")
    LOGIN_BUTTON = (By.XPATH, "//input[@value='Log in']")
    LOGOUT_LINK = (By.LINK_TEXT, "Logout")
