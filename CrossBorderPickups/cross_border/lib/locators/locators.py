from selenium.webdriver.common.by import By


class Locators:
    """ Covers locators of all web page from applications """
    table_column = 'table[class*="table-centered"] thead th'
    table_row = 'table[class*="cursor-pointer"] tbody tr'
    modal_table_row = 'table[class*="table-hover"] tbody tr'
    modal = (By.CSS_SELECTOR, 'div.modal-content')
    ops_modal = (By.CSS_SELECTOR, 'mat-dialog-container[class*="mat-dialog-container"]')
    modal_title = (By.CSS_SELECTOR, 'div.modal-header h4')
    ops_modal_title = (By.CSS_SELECTOR, 'h2[class="mat-dialog-title"]')
    modal_close_button = (By.CSS_SELECTOR, 'div.modal-footer button[class*="btn-light"]')
    modal_close_icon = (By.CSS_SELECTOR, 'button.close')
    modal_back_button = (By.CSS_SELECTOR, 'div.modal-footer button[class*="btn-primary"]')
    drop_down_search_field = (By.CSS_SELECTOR, 'input[id*="search-field"][tabindex="0"]')
    select_drop_down_arrow = (By.CSS_SELECTOR, 'span[role="presentation"]')
    country_origin_list_panel = (By.CSS_SELECTOR, 'div[class*="results"]')
    drop_down_results = 'div[class="select2-results"] li[aria-selected="true"]'
    auto_suggestion_results = 'span.mat-option-text'
    reports_drop_down_arrow = (By.CSS_SELECTOR, 'mat-icon[class*="indicatorRotate"]')

    class Notification:
        """ Locators related to Notifications messages """
        notification_msg_div = (By.CSS_SELECTOR, 'div[class*="notification-msg-opened"]')
        notification_msg_icon = (By.CSS_SELECTOR, 'div[class*="notification-msg-icon"]')
        notification_msg_text = (By.CSS_SELECTOR, 'div[class*="notification-msg-body"]')
        ops_notification_msg_text = (By.CSS_SELECTOR, 'simple-snack-bar.mat-simple-snackbar span')
        notification_close_button = (By.CSS_SELECTOR, 'button[class*="notification-msg-close-button"]')

    class SignUpPage:
        """ Locators related to SignUp page """
        business_user_create_account = (By.CSS_SELECTOR, 'div[class*="ribbon-info"]')
        personal_user_create_account = (By.CSS_SELECTOR, 'div[class*="ribbon-success"]')

    class LoginPage:
        """ Locators related to Login Page """
        email_id = (By.CSS_SELECTOR, 'input[formcontrolname="email"]')
        password = (By.CSS_SELECTOR, 'input[formcontrolname="password"]')
        login_button = (By.CSS_SELECTOR, 'button[type="submit"]')
        user_icon = (By.CSS_SELECTOR, '#profileDropdown')
        logout_button = (By.CSS_SELECTOR, 'a[class="dropdown-item notify-item"]')
        invalid_email_error = (By.CSS_SELECTOR, 'div[class="invalid-feedback"] div')
        email_msg = (By.XPATH, "//div[contains(text(),'Email is required')]")
        password_msg = (By.XPATH, "//div[contains(text(),'Password is required')]")
        credentials_msg = (By.XPATH, "//div[contains(text(),'No active account found with the given credentials')]")

    class ShipmentPage:
        """ Locators related to Shipment Page """
        page_title = (By.CSS_SELECTOR, 'h4[class="page-title"]')

    class PackagesPage:
        """ Locators related to Packages Page """
        page_title = (By.CSS_SELECTOR, 'h4[class="page-title"]')
        no_record_msg = (By.CSS_SELECTOR, 'div[class*="text-center"] h4')
        checkout_button = (By.XPATH, '//button[contains(@class, "btn-primary") and contains(text(), "Checkout")]')
        link_button = (By.XPATH, '//button[contains(@class, "btn-success") and contains(text(), "Link")]')
        unlink_button = (By.XPATH, '//button[contains(@class, "btn-warning") and contains(text(), "Unlink")]')
        discard_button = (By.XPATH, '//button[contains(@class, "btn-danger") and contains(text(), "Discard")]')
        search_package_field = (By.CSS_SELECTOR, 'input[name="searchTerm"]')
        add_content_button = (By.XPATH, '//button[contains(text(), "Add Content")]')
        edit_content_icon = "content-save-edit"
        delete_content_icon = "mdi-delete"

        class CreateOrder:
            """ Locators related to Create Order modal """
            send_to_canada_button = (By.XPATH, '//button[contains(text(), "Send to Canada")]')
            receive_package_method_message = (By.CSS_SELECTOR, 'div[class="my-1"]')
            shipping_address_name = (By.CSS_SELECTOR, 'div[class*="my-1"] input[formcontrolname="name"]')
            select_mail_address = (By.CSS_SELECTOR, '#select-mail-address')
            email_field = (By.CSS_SELECTOR, 'input[formcontrolname="email"]')
            same_billing_address_checkbox = '#sameBillingAddress'
            name_on_card_field = (By.CSS_SELECTOR, 'div[class="form-group"] input[formcontrolname="name"]')
            card_number_field = (By.CSS_SELECTOR, 'input[formcontrolname="number"]')
            exp_date_field = (By.CSS_SELECTOR, 'input[formcontrolname="exp_date"]')
            cvc_field = (By.CSS_SELECTOR, 'input[formcontrolname="cvc"]')
            address_field = (By.CSS_SELECTOR, 'input[formcontrolname="address_line1"]')
            city_field = (By.CSS_SELECTOR, 'div[class="form-group"] input[formcontrolname="address_city"]')
            province_field = (By.CSS_SELECTOR, 'select2[formcontrolname="address_state"] span')
            postal_code_field = (By.CSS_SELECTOR, 'div[class="form-group"] input[formcontrolname="address_zip"]')
            country_field = (By.CSS_SELECTOR, 'select2[formcontrolname="address_country"] span')
            pay_ca_button = (By.XPATH, './/button[contains(text(), "Pay ")]')
            invalid_address_error_msg = (By.CSS_SELECTOR, 'span.text-danger')
            create_order_modal_close_icon = (By.CSS_SELECTOR, 'button.close')

        class AddContent:
            """ Locators related to Add Content modal """
            add_content_modal_title = (By.CSS_SELECTOR, 'h4.modal-title')
            duty_category_field = (By.ID, "typeahead-focus")
            duty_category_list_panel = (By.CSS_SELECTOR, '[class*="dropdown-menu show"][role="listbox"]')
            duty_category_items = 'button[class*="dropdown-item"]'
            quantity_field = (By.CSS_SELECTOR, 'input[formcontrolname="quantity"]')
            value_usd_field = (By.CSS_SELECTOR, 'input[formcontrolname="value_usd"]')
            description_area = (By.CSS_SELECTOR, 'textarea[formcontrolname="description"]')
            add_button = (By.XPATH, '//div[@class="modal-footer"]//button[contains(text(), "Add")]')
            update_button = (By.XPATH, '//div[@class="modal-footer"]//button[contains(text(), "Update")]')
            cancel_button = (By.XPATH, '//div[@class="modal-footer"]//button[contains(text(), "Cancel")]')
            country_origin = (By.CSS_SELECTOR, 'span[class*="selection__rendered"]')

        class DiscardPackage:
            """ Locators related to Discard Package modal """
            discard_button = (By.XPATH, './/div[contains(@class, "tab-pane")]//button[contains(text(), "Discard")]')

    class ShippingOrdersPage:
        """ Locators related to Shipment Orders Page """
        manual_order_entry = (By.XPATH, './/button[contains(text(), "Manual Order Entry")]')

        class ManualOrderEntryModal:
            """ Locators related to Manual Orders Entry modal """
            carrier_label = (By.XPATH, './/label[contains(text(), "Carriers")]')
            tracking_number = (By.CSS_SELECTOR, 'input[formcontrolname="tracking_number"]')
            carriers_drop_down = (By.XPATH, './/select2[@placeholder="Carriers"]//span['
                                            '@class="select2-selection__rendered"]')
            next_button = (By.XPATH, './/button[contains(text(), "Next")]')

    class HeaderPage:
        """ Locators related to Header Page """
        user_avatar = (By.XPATH, './/li[@class="notification-list dropdown"]')
        operation_button = (By.XPATH, './/span[contains(text(), "Operation")]')
        logout_option = (By.XPATH, './/span[contains(text(), "Logout")]')

    class NewPackagesPage:
        """ Locators related to New Packages Page """
        app_package_div = (By.CSS_SELECTOR, 'div.view_container_height')
        full_name = (By.CSS_SELECTOR, 'app-profile-popover[labeltext="Full Name"] input')
        full_name_results = './/span[@class="mat-option-text"]//span[1]/span[@class="text-dark"]'
        date_picker_input_field = (By.CSS_SELECTOR, 'input[class*="mat-datepicker-input"]')
        date_picker_toggle_button = (By.CSS_SELECTOR, 'mat-datepicker-toggle[class*="mat-datepicker-toggle"]')
        date_picker_modal = (By.CSS_SELECTOR, 'mat-calendar[id*="mat-datepicker"]')
        month_year_button = (By.CSS_SELECTOR, 'div[class="mat-calendar-arrow"]')
        calender_body_cell = 'td[role="gridcell"]'
        calender_body_content = 'div[class*="mat-calendar-body-cell-content"]'
        previous_year_button = (By.CSS_SELECTOR, 'button[class*="mat-calendar-previous-button"]')
        next_year_button = (By.CSS_SELECTOR, 'button[class*="mat-calendar-next-button"]')
        tracking_number = (By.CSS_SELECTOR, 'input[formcontrolname="incoming_carrier_tracking_number"]')
        vendor_dropdown = (By.CSS_SELECTOR, 'app-vendor-popover input')
        weight_field = (By.CSS_SELECTOR, 'input[formcontrolname="weight"]')
        length_field = (By.CSS_SELECTOR, 'input[formcontrolname="length"]')
        width_field = (By.CSS_SELECTOR, 'input[formcontrolname="width"]')
        height_field = (By.CSS_SELECTOR, 'input[formcontrolname="height"]')
        package_type = (By.CSS_SELECTOR, 'mat-select[formcontrolname="type"] span[class*="value-text"] span')
        invoice_checkbox = (By.CSS_SELECTOR, 'mat-checkbox[formcontrolname="invoice"] input')
        data_received_checkbox = (By.CSS_SELECTOR, 'mat-checkbox[formcontrolname="data_received"] input')
        add_content_button = (By.XPATH, './/span[@class="mat-button-wrapper" and contains(text(), "Add Content")]')
        package_separation_checkbox = (By.CSS_SELECTOR, 'mat-checkbox[formcontrolname="package_separation"] input')
        create_update_package_button = (By.CSS_SELECTOR, 'button[fxflex="33"]')
        required_field_error_msgs = 'mat-error[class*="mat-error"]'

        class AddContent:
            """ Locators related to "Add Content" modal form """
            content_category_label = './/span[contains(@class, "ng-star-inserted") and contains(' \
                                     'text(), "Category/Description")]'
            category_or_description = (By.CSS_SELECTOR, 'input[data-placeholder="Category/Description"]')
            country_origin_drop_down_arrow = (By.CSS_SELECTOR, 'mat-select[formcontrolname="coo"] div[class*="'
                                                               'mat-select-arrow-wrapper"]')
            content_quantity = (By.CSS_SELECTOR, 'mat-dialog-content input[formcontrolname="quantity"]')
            content_value = (By.CSS_SELECTOR, 'mat-dialog-content input[formcontrolname="value_usd"]')
            content_description = (By.CSS_SELECTOR, 'mat-dialog-content textarea[formcontrolname="description"]')
            add_button = (By.XPATH, './/mat-dialog-actions[@class="mat-dialog-actions"]//button//span[contains('
                                    'text(), "Add")]')
            cancel_button = (By.XPATH, './/mat-dialog-actions[@class="mat-dialog-actions"]//button//span[contains('
                                       'text(), "Cancel")]')
