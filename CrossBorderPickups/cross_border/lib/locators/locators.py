from selenium.webdriver.common.by import By


class Locators:
    """ Covers locators of all web page from applications """

    class SignUpPage:
        """ Locators related to SignUp page """
        sign_up_link = (By.CSS_SELECTOR, "a[href='/account/signup']")
        business_user_create_account = (By.CSS_SELECTOR, 'div[class*="ribbon-info"]')
        personal_user_create_account = (By.CSS_SELECTOR, 'div[class*="ribbon-success"]')
        personal_account = (By.CSS_SELECTOR, 'div[class="ribbon ribbon-info float-right cursor-pointer"]')

    class LoginPage:
        """ Locators related to Login Page """
        email_id = (By.ID, "email")
        password = (By.ID, "password")
        login_button = (By.CSS_SELECTOR, "button[type='submit']")
        user_icon = (By.CSS_SELECTOR, '#profileDropdown')
        logout_button = (By.CSS_SELECTOR, 'a[class="dropdown-item notify-item"]')
        email_msg = (By.XPATH, "//div[contains(text(),'Email is required')]")
        password_msg = (By.XPATH, "//div[contains(text(),'Password is required')]")
        credentials_msg = (By.XPATH, "//div[contains(text(),'No active account found with the given credentials')]")

    class PersonSignUp:
        """ Locators related to Personal account registration """
        fullname = (By.CSS_SELECTOR, "input[formcontrolname='full_name']")
        email = (By.CSS_SELECTOR, "input[type='email']")
        password = (By.CSS_SELECTOR, "input[formcontrolname='password']")
        confirmPassword = (By.CSS_SELECTOR, "input[formcontrolname='confirm_password']")
        phone_number = (By.CSS_SELECTOR, "input[formcontrolname='confirm_password']")
        line1 = (By.CSS_SELECTOR, "input[formcontrolname='home_line_1']")
        line2 = (By.CSS_SELECTOR, "input[formcontrolname='home_line_2']")
        city = (By.CSS_SELECTOR, "input[formcontrolname='home_city']")
        postal_code = (By.CSS_SELECTOR, "input[formcontrolname='home_postal_code']")
        province = (By.CSS_SELECTOR, "div[class='selection select2-focused']")

    class ShipmentPage:
        """ Locators related to Shipment Page """
        page_title = (By.CSS_SELECTOR, 'h4[class="page-title"]')
