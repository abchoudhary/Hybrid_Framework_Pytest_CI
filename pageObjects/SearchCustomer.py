class SearchCustomer:
    textbox_searchEmail_id = "SearchEmail"
    textbox_searchFirstName_id = "SearchFirstName"
    textbox_searchLastName_id = "SearchLastName"
    button_search_id = "search-customers"

    table_search_results_xpath = "//table[@role='grid']"
    table_xpath = "//table[@id='customers-grid']"
    table_rows_xpath = "//table[@id='customers-grid']//tbody/tr"
    table_columns_xpath = "//table[@id='customers-grid']//tbody/tr/td"

    def __init__(self, driver):
        self.driver = driver

    def set_search_email(self, email):
        self.driver.find_element_by_id(self.textbox_searchEmail_id).clear()
        self.driver.find_element_by_id(self.textbox_searchEmail_id).send_keys(email)

    def set_first_name(self, first_name):
        self.driver.find_element_by_id(self.textbox_searchFirstName_id).clear()
        self.driver.find_element_by_id(self.textbox_searchFirstName_id).send_keys(first_name)

    def set_last_name(self, last_name):
        self.driver.find_element_by_id(self.textbox_searchLastName_id).clear()
        self.driver.find_element_by_id(self.textbox_searchLastName_id).send_keys(last_name)

    def click_search(self):
        self.driver.find_element_by_id(self.button_search_id).click()

    def get_row_count(self):
        return len(self.driver.find_elements_by_xpath(self.table_rows_xpath))

    def get_column_count(self):
        return len(self.driver.find_elements_by_xpath(self.table_columns_xpath))

    def search_customer_by_email(self, email):
        flag = False
        for row in range(1, self.get_row_count()+1):
            table = self.driver.find_element_by_xpath(self.table_xpath)
            email_id = table.find_element_by_xpath("//table[@id='customers-grid']/tbody/tr["+str(row)+"]/td[2]").text
            if email_id == email:
                flag = True
                break
        return flag

    def search_customer_by_name(self, exp_name):
        flag = False
        for row in range(1, self.get_row_count()+1):
            table = self.driver.find_element_by_xpath(self.table_xpath)
            name = table.find_element_by_xpath("//table[@id='customers-grid']/tbody/tr["+str(row)+"]/td[3]").text
            if name == exp_name:
                flag = True
                break
        return flag
