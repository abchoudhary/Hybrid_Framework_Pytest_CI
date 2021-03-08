from selenium.webdriver.common.by import By


class AddCustomerLocators:
    CUSTOMER_MENU_LINK = (By.XPATH, "//a[@href='#']//span[contains(text(),'Customers')]")
    CUSTOMER_ITEM_LINK = (By.XPATH, "//span[@class='menu-item-title'][normalize-space()='Customers']")
    ADD_NEW_BUTTON = (By.XPATH, "//a[normalize-space()='Add new']")
    EMAIL_TEXTBOX = (By.ID, "Email")
    PASSWORD_TEXTBOX = (By.ID, "Password")
    FIRSTNAME_TEXTBOX = (By.ID, "FirstName")
    LASTNAME_TEXTBOX = (By.ID, "LastName")
    GENDER_MALE_RADIO = (By.ID, "Gender_Male")
    GENDER_FEMALE_RADIO = (By.ID, "Gender_Female")
    DOB_TEXTBOX = (By.ID, "DateOfBirth")
    COMPANY_TEXTBOX = (By.ID, "Company")
    TAX_CHECKBOX = (By.ID, "IsTaxExempt")

    # Handling textbox with options to choose
    NEWSLETTER_TEXTBOX = (By.XPATH, "(//div[@class='k-multiselect-wrap k-floatwrap'])[1]")
    YOUR_STORE_LIST_ITEM = (By.XPATH, "//li[contains(text(), 'Your store name')]")
    TEST_STORE2_LIST_ITEM = (By.XPATH, "//li[contains(text(), 'Test store 2')]")

    CUSTOMER_ROLES_TEXTBOX = (By.XPATH, "(//div[@class='k-multiselect-wrap k-floatwrap'])[2]")
    ADMINISTRATORS_LIST_ITEM = (By.XPATH, "//li[contains(text(), 'Administrators')]")
    REGISTERED_LIST_ITEM = (By.XPATH, "//li[contains(text(), 'Registered')]")
    GUESTS_LIST_ITEM = (By.XPATH, "//li[contains(text(), 'Guests')]")
    VENDORS_LIST_ITEM = (By.XPATH, "//li[contains(text(), 'Vendors')]")

    VENDOR_DROPDOWN = (By.ID, "VendorId")
    ACTIVE_CHECKBOX = (By.ID, "Active")
    ADMIN_TEXTAREA = (By.ID, "AdminComment")
    SAVE_BUTTON = (By.NAME, "save")
