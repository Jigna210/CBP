import pytest

from CrossBorderPickups.cross_border.lib.constants.constant import PageConstants, BaseConstants
from CrossBorderPickups.cross_border.lib.utility.side_nav import SideNavigation
from CrossBorderPickups.cross_border.page_objects.UI.LoginPage.login_page import LoginPage


@pytest.mark.usefixtures("login")
class TestOperationsPage:
    """
    Covers tests related to Operations page

    Pre-requisite:
        1. Enter url "https://cbp-ops-qa.crossborderpickups.ca/"
        2. Enter username and password
        3. Click on login button
    """

    def test_visibility_of_operations_and_customer_service_menu_in_side_navigation_panel(self, login):
        """
        Test Steps:
            1. Follow only pre-requisite steps

        Scenario Tested:
        [x] User can see "Operations" menu and below sub-menu's after getting login.
            - New Package
            - Packages
            - Customs Forms
            - Scanning Tool
            - Rates
        [x] User can also see "Customer Service" menu and below sub-menu's after getting login.
            - Orders
            - Customer Accounts
        """
        app_url = BaseConstants.OPERATION_PORTAL_URL
        app_user_name = BaseConstants.OPERATION_PORTAL_USERNAME
        app_password = BaseConstants.OPERATION_PORTAL_PASSWORD

        LoginPage(self.driver).login_in_portal_with_credentials(driver_instance=self.driver, portal_url=app_url,
                                                                user_name=app_user_name, password=app_password)

        side_nav_panel_constant = PageConstants.SideNavigationPanel

        side_nav_options_dict = {
            side_nav_panel_constant.OPS_SHOP_AND_SHIP: side_nav_panel_constant.ShopAndShip.OPS_SHOP_AND_SHIP_OPTIONS,
            side_nav_panel_constant.ECOMMERCE_SHIPPING:
                side_nav_panel_constant.EcommerceShipping.ECOMMERCE_SHIPPING_OPTIONS,
            side_nav_panel_constant.CUSTOMER_SERVICE: [side_nav_panel_constant.CustomerService.CUSTOMER_ACCOUNT],
            side_nav_panel_constant.ADMIN_PANEL: side_nav_panel_constant.AdminPanel.USER_ACCOUNT_MANAGEMENT}

        side_nav_panel = SideNavigation(self.driver)

        for side_nav_menu, side_nav_sub_menu in side_nav_options_dict.items():
            side_nav_menu_element = side_nav_panel.get_element_of_side_nav_panel(menu=side_nav_menu)

            assert side_nav_panel.is_element_visible(by_locator=side_nav_menu_element), \
                "'{}' menu is getting missing or mismatched on side navigation panel.".format(side_nav_menu)

            for option in side_nav_sub_menu:
                sub_menu_element = side_nav_panel.get_element_of_side_nav_option(
                    menu=side_nav_menu, sub_menu=option)

                assert side_nav_panel.is_element_visible(by_locator=sub_menu_element), \
                    "'{}' option is getting missing or mismatched under '{}' menu on side navigation panel.".format(
                        option, side_nav_menu)
