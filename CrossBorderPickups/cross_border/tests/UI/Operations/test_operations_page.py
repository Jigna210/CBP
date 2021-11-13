import pytest

from CrossBorderPickups.cross_border.lib.constants.constant import PageConstants
from CrossBorderPickups.cross_border.lib.utility.side_nav import SideNavigation


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
        side_nav_panel = SideNavigation(self.driver)
        ops_menu_constant = PageConstants.SideNavigationPanel.Operations
        cs_menu_constant = PageConstants.SideNavigationPanel.CustomerService

        for sub_menu in [ops_menu_constant.NEW_PACKAGE, ops_menu_constant.PACKAGES, ops_menu_constant.CUSTOMS_FORMS,
                         ops_menu_constant.SCANNING_TOOL, ops_menu_constant.RATES, cs_menu_constant.ORDERS,
                         cs_menu_constant.CUSTOMER_ACCOUNT]:
            sub_menu_element = side_nav_panel.get_element_of_side_navigation_option(
                menu=PageConstants.SideNavigationPanel.OPERATIONS, sub_menu=sub_menu)

            assert side_nav_panel.is_element_visible(by_locator=sub_menu_element), \
                "'{}' menu is getting missing or mismatched on side navigation panel.".format(sub_menu)
