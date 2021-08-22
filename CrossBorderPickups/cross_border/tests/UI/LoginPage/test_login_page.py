from cross_border.lib.locators.locators import Locators
from cross_border.page_objects.UI.LoginPage.login_page import LoginPage
from cross_border.page_objects.UI.ShipmentPage.shipment_page import ShipmentPage
from cross_border.tests.test_base import BaseTest


class TestLoginPage(BaseTest):
    """ Covers tests related to user login """

    def test_user_can_login_successfully(self):
        """
        Test Steps:
        1. Enter correct username or email id
        2. Enter correct password
        3. Click on Login button

        Scenario Tested:
        [x] User should do login successfully in product.
        """
        login_page = LoginPage(self.driver)
        login_page.do_login()

        shipment_page = ShipmentPage(self.driver)
        page_title = shipment_page.get_element_text(by_locator=Locators.ShipmentPage.page_title)

        assert page_title == "Shipments", "User can not be login successfully"
