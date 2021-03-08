from selenium.webdriver.common.by import By


class SearchCustomerLocators:
    SEARCH_EMAIL_TEXTBOX = (By.ID, "SearchEmail")
    SEARCH_FIRSTNAME_TEXTBOX = (By.ID, "SearchFirstName")
    SEARCH_LASTNAME_TEXTBOX = (By.ID, "SearchLastName")
    SEARCH_BUTTON = (By.ID, "search-customers")

    SEARCH_RESULTS_TABLE = (By.XPATH, "//table[@role='grid']")
    GRID_TABLE = (By.XPATH, "//table[@id='customers-grid']")
    ROWS_TABLE = (By.XPATH, "//table[@id='customers-grid']//tbody/tr")
    COLUMNS_TABLE = (By.XPATH, "//table[@id='customers-grid']//tbody/tr/td")
