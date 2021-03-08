from Resources.Locators_SearchCustomer import SearchCustomerLocators


class SearchCustomer:
    def __init__(self, driver):
        self.driver = driver

    def set_search_email(self, email):
        self.driver.find_element(*SearchCustomerLocators.SEARCH_EMAIL_TEXTBOX).clear()
        self.driver.find_element(*SearchCustomerLocators.SEARCH_EMAIL_TEXTBOX).send_keys(email)

    def set_first_name(self, first_name):
        self.driver.find_element(*SearchCustomerLocators.SEARCH_FIRSTNAME_TEXTBOX).clear()
        self.driver.find_element(*SearchCustomerLocators.SEARCH_FIRSTNAME_TEXTBOX).send_keys(first_name)

    def set_last_name(self, last_name):
        self.driver.find_element(*SearchCustomerLocators.SEARCH_LASTNAME_TEXTBOX).clear()
        self.driver.find_element(*SearchCustomerLocators.SEARCH_LASTNAME_TEXTBOX).send_keys(last_name)

    def click_search(self):
        self.driver.find_element(*SearchCustomerLocators.SEARCH_BUTTON).click()

    def get_row_count(self):
        return len(self.driver.find_elements(*SearchCustomerLocators.ROWS_TABLE))

    def get_column_count(self):
        return len(self.driver.find_elements(*SearchCustomerLocators.COLUMNS_TABLE))

    def search_customer_by_email(self, email):
        flag = False
        for row in range(1, self.get_row_count()+1):
            table = self.driver.find_element(*SearchCustomerLocators.GRID_TABLE)
            email_id = table.find_element_by_xpath("//table[@id='customers-grid']/tbody/tr["+str(row)+"]/td[2]").text
            if email_id == email:
                flag = True
                break
        return flag

    def search_customer_by_name(self, exp_name):
        flag = False
        for row in range(1, self.get_row_count()+1):
            table = self.driver.find_element(*SearchCustomerLocators.GRID_TABLE)
            name = table.find_element_by_xpath("//table[@id='customers-grid']/tbody/tr["+str(row)+"]/td[3]").text
            if name == exp_name:
                flag = True
                break
        return flag
