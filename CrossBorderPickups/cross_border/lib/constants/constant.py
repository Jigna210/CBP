
class BaseConstants:
    """ Common application constants """
    DEFAULT_BASE_URL = "https://cbp-customer-qa.crossborderpickups.ca/"
    CUSTOMER_USER_NAME = "qa_test12@yopmail.com"
    DEFAULT_PASSWORD = "123456"
    DEFAULT_TIMEOUT = 30
    CHROME_BROWSER = "Chrome"
    CHROME_BINARY_LOCATION = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe"
    FIREFOX_BROWSER = "Firefox"
    LOCAL = "Local"
    GRID = "Grid"
    WINDOWS_SYSTEM = "Windows"
    DISCARD_CHARGE_PER_PACKAGE = 2
    ERROR_COLOR_CODE = "#F44336"
    SCREENSHOT_EXTENSION = "png"

    class Urls:
        """ Constants related to application page URL's """
        # GRID_HUB_URL = "http://ec2-3-16-166-56.us-east-2.compute.amazonaws.com:4444/wd/hub"
        GRID_HUB_URL = "https://localhost:4444/wd/hub/"
        LOGIN_PAGE_URL = "account/auth/login"
        PACKAGES_PAGE_URL = "packages"
        DASHBOARD_PAGE_URL = "customerDashboard"
        ORDERS_PAGE_URL = "orders"
        PROFILE_PAGE_URL = "profile"
        SHIPPING_ORDERS_PAGE_URL = "ecommerce/orders"
        NEW_PACKAGES_PAGE_URL = "packages/add"
        OPS_PACKAGES_PAGE_URL = "packages"
        CUSTOMS_FORM_PAGE_URL = "customsForms"
        SCANNING_TOOL_PAGE_URL = "scanningTool"
        RATES_PAGE_URL = "rates"

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
        PENDING_ORDER_CREATION = "Pending Order Creation"
        CANADIAN_PROVINCES = ["Alberta", "British Columbia", "Manitoba", "New Brunswick", "Newfoundland and Labrador",
                              "Northwest Territories", "Nova Scotia", "Nunavut", "Ontario", "Prince Edward Island",
                              "Quebec", "Saskatchewan", "Yukon"]
        CANADIAN_CITIES = ["Airdrie", "Beaumont", "Brooks", "Calgary", "Camrose", "Chestermere", "Cold Lake",
                           "Edmonton", "Fort Saskatchewan", "Grande Prairie", "Lacombe", "Leduc", "Lethbridge",
                           "Lloydminster", "Medicine Hat", "Red Deer", "Spruce Grove", "St. Albert", "Wetaskiwin"]
        POSTAL_CODES = []

        class AddContent:
            """ Constants related to Packages Content table """
            CONTENT_QTY = "Qty"
            CONTENT_VALUE = "Value"
            CONTENT_TOTAL_VALUE = "Total Value"
            CONTENT_TOTAL_VALUE_CAD = "Total Value(CAD)"
            CONTENT_EST_DUTIES = "Est. Duties"
            CONTENT_EST_TAX = "Est. Tax"

        class CreateOrder:
            """ Constants related to Create Order modal """
            PACKAGE_RECEIVE_METHOD_MESSAGE = "How would you like to receive the package ?"
            PACKAGE_RECEIVE_BY_MAIL = "Mail"
            PACKAGE_RECEIVE_BY_PICKUP = "Pickup"
            PACKAGE_PICKUP_LOCATION_MISSISSAUGA = "Mississauga"
            PACKAGE_PICKUP_LOCATION_MARKHAM = "Markham"
            PAYMENT_CARD_NUMBERS = ["3782822463100050", "5555555555554444", "4242424242424242"]

        class DiscardPackages:
            """ Constants related to Discard packages modal """
            NUMBER_OF_DISCARDS = "Number of Discards"
            TOTAL_CHARGE = "Total Charge"

    class NewPackagePage:
        """ Constants related to New Package page """
        FULL_NAME = "Full Name"
        STATUS_FOR_POSTING = "Status for Posting"
        DATE_RECEIVED = "Date Received"
        CARRIER = "Carrier"
        TRACKING_NUMBER = "Tracking Number"
        VENDOR = "Vendor"
        WEIGHT = "Weight"
        REQUIRED_FIELDS = [FULL_NAME, STATUS_FOR_POSTING, DATE_RECEIVED, CARRIER, TRACKING_NUMBER, VENDOR, WEIGHT]

        class PackageStatus:
            """ Constants related to Package Status from New Package page """
            INFORMATION_REQUIRED = "Information Required"
            PENDING_ORDER_CREATION = "Pending Order Creation"
            STATUSES_FOR_POSTING = [INFORMATION_REQUIRED, PENDING_ORDER_CREATION]

        class PackageCarrier:
            """ Constants related to Package Carrier from New Package page """
            UPS = "UPS"
            USPS = "USPS"
            FED_EX = "Fed Ex"
            DHL = "DHL"
            AMAZON_LOGISTICS = "AMAZON LOGISTICS"
            FREIGHT = "FREIGHT"
            CENTRAL_TRANSPORT = "Central Transport"
            WALK_IN = "Walk-In"
            LASER_SHIP = "Laser Ship"
            CARRIERS = [UPS, USPS, FED_EX, DHL, AMAZON_LOGISTICS, FREIGHT, CENTRAL_TRANSPORT, WALK_IN, LASER_SHIP]

        class PackageVendors:
            """ Constants related to Package Vendors from New Package page """
            UA = "UA"
            MACY = "MACY"
            WALMART_COM = "WALMART.COM"
            AOSOM = "AOSOM"
            JLS = "JUSTIFIED LOGISTICS SOLUTIONS"
            FULL_MOON_EMPIRE = "FULL MOON EMPIRE"
            KRAFT_WERKS = "KRAFT WERKS"
            BOB_KING = "BOB KING"
            MERCOLA_COM = "MERCOLA.COM"
            BAY_LAKE = "BAY LAKE"
            VENDORS = [UA, MACY, WALMART_COM, AOSOM, JLS, FULL_MOON_EMPIRE, KRAFT_WERKS, BOB_KING, MERCOLA_COM,
                       BAY_LAKE]

        class PackageCondition:
            """ Constants related to Package condition from New Package page """
            NEW = "New"
            USED = "Used"
            RETURNS = "Returns"
            PACKAGE_CONDITIONS = [NEW, USED, RETURNS]

        class AddContent:
            """ Constants related to "Add Content" form from New Package page """
            CATEGORY_DESCRIPTION = "Category/Description"
            QUANTITY = "Quantity"
            VALUE = "Value(each in USD)"
            ADD_BUTTON = "Add"
            CANCEL_BUTTON = "Cancel"
            REQUIRED_FIELDS = [CATEGORY_DESCRIPTION, QUANTITY, VALUE]

            ZIPPERS = "Zippers"
            ZIPPER_PARTS = "Zipper Parts"
            YOGA_PANTS = "Yoga Pants"
            YEAST = "Yeast (active and inactive)"
            YARNS_OF_WOOL = "Yarns of wool"
            YARNS_OF_COTTON = "Yarns of cotton"
            YARN_PAPER = "Yarn paper"
            YARN_OF_WOOD = "Yarn of wood"
            YARN_OF_SYNTHETIC_FIBRE = "Yarn of synthetic fibre"
            YARN_OF_POLYSTER = "Yarn of polyster"
            CONTENT_CATEGORY = [ZIPPERS, ZIPPER_PARTS, YOGA_PANTS, YEAST, YARNS_OF_WOOL, YARNS_OF_COTTON, YARN_PAPER,
                                YARN_OF_WOOD, YARN_OF_SYNTHETIC_FIBRE, YARN_OF_POLYSTER]

    class SideNavigationPanel:
        """ Constants related to Side navigation panel """
        SHOP_AND_SHIP = "Shop & Ship"
        ECOMMERCE = "Ecommerce"
        PROFILE = "Profile"
        OPERATIONS = "Operations"
        CUSTOMER_SERVICE = "Customer Service"

        class ShopAndShip:
            """ Constants related to Shop & Ship menu """
            DASHBOARD = "Dashboard"
            PACKAGES = "Packages"
            ORDERS = "Orders"

        class Ecommerce:
            """ Constants related to Ecommerce menu """
            DASHBOARD = "Dashboard"
            ORDERS = "Orders"
            SHIPMENT_BATCHES = "Shipment Batches"

        class Operations:
            """ Constants related to Operations menu """
            NEW_PACKAGE = "New Package"
            PACKAGES = "Packages"
            CUSTOMS_FORMS = "Customs Forms"
            SCANNING_TOOL = "Scanning Tool"
            RATES = "Rates"

        class CustomerService:
            """ Constants related to Customer Service menu """
            ORDERS = "Orders"
            CUSTOMER_ACCOUNT = "Customer Account"
