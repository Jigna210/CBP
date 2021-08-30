import random

import pytest

from CrossBorderPickups.cross_border.lib.constants.constant import PageConstants
from CrossBorderPickups.cross_border.lib.locators.locators import Locators
from CrossBorderPickups.cross_border.page_objects.UI.PackagesPage.packages_page import PackagesPage, PackagesList, \
    CreateOrderModal
from CrossBorderPickups.cross_border.tests.test_base import BaseTest


class TestPackagesPage(BaseTest):
    """
    Covers tests related to packages page

    Pre-requisite:
        1. Enter url "https://www.crossborderpickups.ca/"
        2. Click on login button
        3. Enter username
        4. Enter password
        5. Click on login button
    """

    def select_packages_from_packages_list_table(self, select_action: str = "single", return_ids: bool = False) -> list:
        """
        Helper function to select packages from packages list table

        :param str select_action: action value like single/multiple
        :param bool return_ids: True if selected package ids needed else False
        :return: selected package's id
        :rtype: list
        """
        packages_page = PackagesPage(self.driver)
        packages_page.wait_for_element(lambda: packages_page.is_element_visible(
            by_locator=Locators.PackagesPage.create_order_button), waiting_for="packages page gets loaded")

        packages_list = PackagesList(self.driver)
        package_ids = packages_list.get_all_packages_id()

        number_of_package = 1 if (select_action == "single" or len(package_ids)) == 1 else \
            random.randint(2, len(package_ids))
        expected_ids = random.sample(package_ids, k=number_of_package)

        for package_id in expected_ids:
            packages_list.select_package_by_id(package_id=package_id)

        return expected_ids if return_ids else None

    @pytest.mark.xfail
    def test_verify_empty_record_message_while_no_records(self):
        """
        Test Steps:
            1. Go to Packages page
            2. Enter value in Search textbox

        Scenario Tested:
        [x] Verify if no record is exist then "no record" message should appear
        """
        packages_page = PackagesPage(self.driver)
        expected_message = packages_page.get_element_text(by_locator=Locators.PackagesPage.no_record_msg)

        assert expected_message == PageConstants.PackagesPage.NO_RECORD_MESSAGE, \
            "'No Records' message is not showing even if there is no records found."

    @pytest.mark.parametrize('select_action', ['single', 'multiple'])
    def test_user_can_select_single_or_multiple_packages(self, select_action):
        """
        Test Steps:
            1. Go to Packages page
            2. Select single or multiple packages from packages list table

        Scenario Tested:
        [x] User should select single and multiple packages that, we want to ship
        """
        selected_ids = self.select_packages_from_packages_list_table(select_action=select_action, return_ids=True)

        for package_id in selected_ids:
            assert PackagesList(self.driver).get_element_of_package_checkbox(package_id=package_id).is_selected(), \
                "Failed to select package by using checkbox."

    @pytest.mark.parametrize('select_action', ['single', 'multiple'])
    def test_user_can_create_order_by_selecting_single_or_multiple_packages(self, select_action):
        """
        Test Steps:
            1. Go to Packages page
            2. Select single or multiple packages from packages list table

        Scenario Tested:
        [x] User should select single and multiple packages that, we want to ship
        """
        selected_ids = self.select_packages_from_packages_list_table(select_action=select_action, return_ids=True)

        packages_page = PackagesPage(self.driver)
        packages_page.click(by_locator=Locators.PackagesPage.create_order_button)

        assert packages_page.is_element_visible(by_locator=Locators.modal), \
            "'Create Order' modal is not getting displayed after clicking on 'Create Order' button by selecting " \
            "single or multiple packages."

        create_order = CreateOrderModal(self.driver)
        create_order_constant = Locators.PackagesPage.CreateOrder
        create_order.wait_for_element(lambda: create_order.is_element_visible(
            by_locator=create_order_constant.send_to_canada_button), waiting_for="create order modal gets loaded")

        assert not create_order.is_element_enabled(by_locator=create_order_constant.send_to_canada_button), \
            "'Send to Canada' button is showing enabled even if no package selected there."

        for package_id in selected_ids:
            PackagesList(self.driver).select_package_by_id(package_id=package_id, element_on_modal=True)

        assert create_order.is_element_enabled(by_locator=create_order_constant.send_to_canada_button), \
            "'Send to Canada' button is not showing enabled even after selecting the packages."

        create_order.click(by_locator=create_order_constant.send_to_canada_button)
        create_order.wait_for_element(lambda: create_order.is_element_visible(
            by_locator=create_order_constant.email_field), waiting_for="order details page gets loaded")

    def test_user_can_view_content_declaration_block(self):
        """
        Test Steps:
            1. Go to Packages page
            2. Select any record from packages list

        Scenario Tested:
        [x] Verify that user should view content declaration blocks
        [x] Verify that User should view package details by selecting a records
        """
        selected_ids = self.select_packages_from_packages_list_table(return_ids=True)[0]

        package_list = PackagesList(self.driver)
        package_content_title_element = package_list.get_element_of_content_block_title(package_id=selected_ids)
        package_content_table_element = package_list.get_element_of_package_content_table(package_id=selected_ids)

        assert all([package_content_title_element.is_displayed(), package_content_table_element.is_displayed(),
                    package_content_title_element.text == PageConstants.PackagesPage.PACKAGE_CONTENTS,
                    package_list.is_element_visible(by_locator=Locators.PackagesPage.add_content_button)]), \
            "'Package Contents' block does not getting opened after selecting package from package list."
