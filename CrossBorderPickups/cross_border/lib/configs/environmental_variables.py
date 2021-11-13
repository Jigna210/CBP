import os

from CrossBorderPickups.cross_border.lib.constants.constant import BaseConstants


class CBP:
    """ Product test environmental related variables """

    CBP_TEST_ENVIRONMENT = os.getenv("CBP_TEST_ENVIRONMENT", default=BaseConstants.LOCAL)
    CBP_TEST_BROWSER = os.getenv("CBP_TEST_BROWSER", default=BaseConstants.CHROME_BROWSER)
    APPLICATION_URL = os.getenv("CBP_BASE_URL", default=BaseConstants.DEFAULT_BASE_URL)
    CBP_USERNAME = os.getenv("CBP_USERNAME", default=BaseConstants.CUSTOMER_USER_NAME)
    CBP_PASSWORD = os.getenv("CBP_PASSWORD", default=BaseConstants.DEFAULT_PASSWORD)
