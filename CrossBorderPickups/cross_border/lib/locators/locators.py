from selenium.webdriver.common.by import By


class Locators:
    """ Covers locators of all web page from applications """

    class SignUpPage:
        """ Locators related to SignUp page """
        business_user_create_account = (By.CSS_SELECTOR, 'div[class*="ribbon-info"]')
        personal_user_create_account = (By.CSS_SELECTOR, 'div[class*="ribbon-success"]')

    class LoginPage:
        """ Locators related to Login Page """
        email_id = (By.ID, "email")
        password = (By.ID, "password")
        login_button = (By.CSS_SELECTOR, "button[type='submit']")

    class ShipmentPage:
        """ Locators related to Shipment Page """
        page_title = (By.CSS_SELECTOR, 'h4[class="page-title"]')
