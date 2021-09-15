class BaseConstants:
    """ Common application constants """
    DEFAULT_TIMEOUT = 40
    BROWSER = "chrome"
    table_column = 'table[class*="table-centered"] thead th'
    table_row = 'table[class*="table-centered"] tbody tr'

    class Urls:
        """ Constants related to application page URL's """
        BASE_URL = "https://cbp-customer-qa.crossborderpickups.ca/"
        LOGIN_PAGE_URL = "/account/auth/login"
        PACKAGES_PAGE_URL = "/packages"
        DASHBOARD_PAGE_URL = "/customerDashboard"
        ORDERS_PAGE_URL = "/orders"
        PROFILE_PAGE_URL = "/profile"

    class Credentials:
        """ Constants related to application credentials """
        USER_NAME = "chavdajigna985@gmail.com"
        PASSWORD = "123456"


class PageConstants:
    """ Constants related to different application web pages """

    class PackagesPage:
        """ Constants related to Packages Page """
        NO_RECORD_MESSAGE = "No Records"
        PACKAGE_STATUS = "Status"
        PACKAGE_RECEIVED_DATE = "Received"
        PACKAGE_SIZE = "Size"
        PACKAGE_TRACKING_NUMBER = "Tracking Number"
        PACKAGE_CARRIER = "Carrier"
        PACKAGE_CONTENTS = "PACKAGE CONTENTS"

        class CreateOrder:
            """ Constants related to Create Order modal """
            PACKAGE_RECEIVE_METHOD_MESSAGE = "How would you like to receive the package ?"
            PACKAGE_RECEIVE_BY_MAIL = "Mail"
            PACKAGE_RECEIVE_BY_PICKUP = "Pickup"
            PACKAGE_PICKUP_LOCATION_MISSISSAUGA = "Mississauga"
            PACKAGE_PICKUP_LOCATION_MARKHAM = "Markham"
