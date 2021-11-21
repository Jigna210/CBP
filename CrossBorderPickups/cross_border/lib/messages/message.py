class NotificationMessages:
    """ Covers notifications from all web pages in applications """

    class LoginPageValidation:
        """ Validation Message for Login page """
        email_required = "Email is required"
        invalid_email_error = "Email must be a valid email address"
        password_required = "Password is required"
        invalid_credentials = "No active account found with the given credentials"

    class PackagesPage:
        """ Notifications messages from Packages page """
        add_content_success_msg = "Package Content added successfully"
        update_content_success_msg = "Package Content updated successfully"
        create_order_success_msg = "Order created successfully"
        discard_package_success_msg = "Package discarded successfully"
        link_packages_error_msg = "You cannot link packages with different Vendors"
        link_packages_success_msg = "Package link successful"
        unlink_packages_success_msg = "Package unlink successful"

    class NewPackagePage:
        """ Notifications messages from New Packages page """
        create_package_success_msg = "Package created"
        full_name_error_msg = "Account is required"
        pkg_status_error_msg = "Status is required"
        date_received_error_msg = "Received Date is required"
        carrier_error_msg = "Carrier is required"
        tracking_number_error_msg = "Tracking number is required"
        vendor_error_msg = "Vendor is required"
        weight_error_msg = "Weight is required"
