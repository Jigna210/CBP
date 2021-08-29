from selenium.webdriver.common.by import By


class Locators:
    """ Covers locators of all web page from applications """
    modal = (By.CSS_SELECTOR, 'div.modal-content')
    modal_title = (By.CSS_SELECTOR, 'div.modal-header h4')
    modal_close_button = (By.CSS_SELECTOR, 'div.modal-footer button[class*="btn-light"]')
    modal_close_icon = (By.CSS_SELECTOR, 'button.close')
    modal_back_button = (By.CSS_SELECTOR, 'div.modal-footer button[class*="btn-primary"]')

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

    class PackagesPage:
        """ Locators related to Packages Page """
        page_title = (By.CSS_SELECTOR, 'h4[class="page-title"]')
        no_record_msg = (By.CSS_SELECTOR, 'div[class*="text-center"] h4')
        create_order_button = (By.XPATH, '//button[contains(@class, "btn-primary") and contains(text(), '
                                         '"Create Order")]')
        add_content_button = (By.XPATH, '//button[contains(text(), "Add Content")]')

        class CreateOrder:
            """ Locators related to Create Order modal """
            send_to_canada_button = (By.XPATH, '//button[contains(text(), "Send to Canada")]')
            email_field = (By.CSS_SELECTOR, 'input[formcontrolname="email"]')
            name_on_card_field = (By.CSS_SELECTOR, 'input[formcontrolname="name"]')
            card_number_field = (By.CSS_SELECTOR, 'input[formcontrolname="number"]')
            exp_month_field = (By.CSS_SELECTOR, 'input[formcontrolname="exp_month"]')
            exp_year_field = (By.CSS_SELECTOR, 'input[formcontrolname="exp_year"]')
            cvc_field = (By.CSS_SELECTOR, 'input[formcontrolname="cvc"]')
            address_field = (By.CSS_SELECTOR, 'input[formcontrolname="address_line1"]')
            city_field = (By.CSS_SELECTOR, 'input[formcontrolname="address_city"]')
            state_field = (By.CSS_SELECTOR, 'input[formcontrolname="address_state"]')
            postal_code_field = (By.CSS_SELECTOR, 'input[formcontrolname="address_zip"]')
            region_selection_arrow = (By.CSS_SELECTOR, 'span[role="presentation"]')
            region_text_field = (By.CSS_SELECTOR, 'input[role="textbox"]')
            region_results = (By.CSS_SELECTOR, 'ul[class*="results"] li')

    class HeaderPage:
        """ Locators related to Header Page """
        user_avatar = (By.CSS_SELECTOR, 'span.account-user-avatar')
        logout_option = (By.CSS_SELECTOR, 'a.dropdown-item.notify-item')
