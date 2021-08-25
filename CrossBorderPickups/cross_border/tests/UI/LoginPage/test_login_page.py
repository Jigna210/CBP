import pytest

from CrossBorderPickups.cross_border.lib.locators.locators import Locators
from CrossBorderPickups.cross_border.lib.messages.message import NotificationMessages
from CrossBorderPickups.cross_border.page_objects.UI.LoginPage.login_page import LoginPage
from CrossBorderPickups.cross_border.page_objects.UI.ShipmentPage.shipment_page import ShipmentPage
from CrossBorderPickups.cross_border.tests.test_base import BaseTest


class TestLoginPage(BaseTest):
    """ Covers tests related to user login """

    def test_user_can_login_with_default_credentials(self):
        """
        Test Steps:
        1. Enter correct username or email id
        2. Enter correct password
        3. Click on Login button

        Scenario Tested:
        [x] User do login successfully in product with default credentials.
        """
        login_page = LoginPage(self.driver)
        login_page.do_login()

        shipment_page = ShipmentPage(self.driver)
        page_title = shipment_page.get_element_text(by_locator=Locators.ShipmentPage.page_title)

        assert page_title == "Shipments", "User can not be login successfully"

        login_page.do_logout()

    @pytest.mark.parametrize('input_username, input_password',
                             [
                                 ('chavdajigna985@gmail.com', '123456'),
                                 ('test@cbp.com', '123456'),
                             ]
                             )
    def test_user_can_login_with_credentials(self, input_username, input_password):
        """
        Test Steps:
        1. Enter correct username or email id
        2. Enter correct password
        3. Click on Login button

        Scenario Tested:
        [x] User should do login successfully in product.
        """
        login_page = LoginPage(self.driver)
        login_page.login_with_credentials(input_username, input_password)

        shipment_page = ShipmentPage(self.driver)
        page_title = shipment_page.get_element_text(by_locator=Locators.ShipmentPage.page_title)

        assert page_title == "Shipments", "User can not be login successfully"

        login_page.do_logout()

    def test_login_blank_credentials(self):
        """
        Test Steps:
        1. Keep blank Email
        2. Keep blank Password
        3. Click on Login Button

        Scenario Tested:
        [x] User should not do login in application with blank credentials.
        """

        login_page = LoginPage(self.driver)
        login_page.login_with_credentials('', '')

        assert login_page.get_element_text(by_locator=Locators.LoginPage.email_msg) == \
               NotificationMessages.LoginPageValidation.Email_required
        assert login_page.get_element_text(by_locator=Locators.LoginPage.password_msg) == \
               NotificationMessages.LoginPageValidation.Password_required

    @pytest.mark.parametrize('input_username, input_password',
                             [
                                 ('chavdajigna985@gmail.com', '12345'),
                                 ('test@cbp', '123456'),
                                 ('jr21029', '123456')
                             ]
                             )
    def test_login_invalid_credentials(self, input_username, input_password):
        """
        Test Steps:
        1. Keep blank Email
        2. Keep blank Password
        3. Click on Login Button

        Scenario Tested:
        [x] User should not do login in application with invalid credentials.
        """

        login_page = LoginPage(self.driver)
        login_page.login_with_credentials(input_username, input_password)

        assert login_page.get_element_text(by_locator=Locators.LoginPage.credentials_msg) == \
               NotificationMessages.LoginPageValidation.Invalid_credentials

    def test_sign_page_with_personal_account(self):
        """
            Test Steps:
            1. Enter Full Name
            2. Enter email
            3. Enter Password
            4. Enter Confirm Password
            5. Enter Phone Number
            6. Enter Address
            7. Enter City
            8. Enter Postal Code
            9. Enter Province
            10.Enter Country

            Scenario Tested:
            [x] User do Sign-Up successfully in application.
       """
        login_page = LoginPage(self.driver)
        login_page.do_user_can_sign_up_personal_account()
