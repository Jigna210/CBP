from typing import Tuple

from selenium.webdriver.common.by import By


class Locators:
    """ Covers locators of all web page from applications """
    modal = (By.CSS_SELECTOR, 'div.modal-content')
    modal_title = (By.CSS_SELECTOR, 'div.modal-header h4')
    modal_close_button = (By.CSS_SELECTOR, 'div.modal-footer button[class*="btn-light"]')
    modal_close_icon = (By.CSS_SELECTOR, 'button.close')
    modal_back_button = (By.CSS_SELECTOR, 'div.modal-footer button[class*="btn-primary"]')
    table_column = 'table[class*="table-centered"] thead th'
    table_row = 'table[class*="table-centered"] tbody tr'
    drop_down_search_field = (By.CSS_SELECTOR, 'input[id*="search-field"]')
    select_drop_down_arrow = (By.CSS_SELECTOR, 'span[role="presentation"]')
    country_origin_list_panel = (By.CSS_SELECTOR, 'div[class*="results"]')
    drop_down_results = 'div[class*="results"] div[class*="label-content"]'
    notification_msg_div = (By.CSS_SELECTOR, 'div[class*="notification-msg-opened"]')
    notification_msg_icon = (By.CSS_SELECTOR, 'div[class*="notification-msg-icon"]')
    notification_msg_text = (By.CSS_SELECTOR, 'div[class*="notification-msg-body"]')

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
        link_button = (By.XPATH, '//button[contains(@class, "btn-success") and contains(text(), "Link")]')
        unlink_button = (By.XPATH, '//button[contains(@class, "btn-warning") and contains(text(), "Unlink")]')
        discard_button = (By.XPATH, '//button[contains(@class, "btn-danger") and contains(text(), "Discard")]')
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
            receive_package_method_message = (By.CSS_SELECTOR, 'div[class="my-1"]')
            shipping_address_name = (By.CSS_SELECTOR, 'div[class*="my-1"] input[formcontrolname="name"]')
            shipping_address_line_1 = (By.CSS_SELECTOR, 'div[class*="my-1"] input[formcontrolname="address_line1"]')
            shipping_address_line_2 = (By.CSS_SELECTOR, 'input[class="form-control"]')
            shipping_address_city = (By.CSS_SELECTOR, 'div[class*="my-1"] input[formcontrolname="address_city"]')
            shipping_address_province = (By.CSS_SELECTOR, 'div[role="combobox"] span[title="Ontario"]')
            shipping_address_postal_code = (By.CSS_SELECTOR, 'div[class*="my-1"] input[formcontrolname="address_zip"]')
            shipping_address_country = (By.CSS_SELECTOR, 'div[role="combobox"] span[title="Canada"]')
            country_field = (By.CSS_SELECTOR, 'div[role="combobox"]')
            pay_ca_button = (By.CSS_SELECTOR, 'form[class*="ng-pristine"] button[class*="btn-block"]')

        class AddContent:
            """ Locators related to Add Content modal """
            duty_category_field = (By.ID, "typeahead-focus")
            duty_category_list_panel = (By.CSS_SELECTOR, '[class*="dropdown-menu show"][role="listbox"]')
            duty_category_items = 'button[class*="dropdown-item"]'
            quantity_field = (By.CSS_SELECTOR, 'input[formcontrolname="quantity"]')
            value_usd_field = (By.CSS_SELECTOR, 'input[formcontrolname="value_usd"]')
            description_area = (By.CSS_SELECTOR, 'textarea[formcontrolname="description"]')
            add_button = (By.XPATH, '//div[@class="modal-footer"]//button[contains(text(), "Add")]')
            cancel_button = (By.XPATH, '//div[@class="modal-footer"]//button[contains(text(), "Cancel")]')
            country_origin = (By.CSS_SELECTOR, 'span[class*="selection__rendered"]')


    class HeaderPage:
        """ Locators related to Header Page """
        user_avatar = (By.CSS_SELECTOR, 'span.account-user-avatar')
        logout_option = (By.CSS_SELECTOR, 'a.dropdown-item.notify-item')
