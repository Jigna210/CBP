import random

import pytest
from selenium.webdriver.common.keys import Keys

from CrossBorderPickups.cross_border.lib.constants.constant import BaseConstants, PageConstants
from CrossBorderPickups.cross_border.lib.helpers.helpers import sleep_execution
from CrossBorderPickups.cross_border.lib.locators.locators import Locators
from CrossBorderPickups.cross_border.lib.messages.message import NotificationMessages
from CrossBorderPickups.cross_border.lib.utility.notification import Notifications
from CrossBorderPickups.cross_border.page_objects.UI.Operations.NewPackagesPage.new_packages_page import NewPackagesPage


@pytest.mark.usefixtures("login")
class TestNewPackagesPage:
    """
    Covers tests related to New Packages page

    Pre-requisite:
        1. Enter url "https://cbp-ops-qa.crossborderpickups.ca/"
        2. Enter username and password
        3. Click on login button
    """
    new_package_constant = PageConstants.NewPackagePage
    new_package_locator = Locators.NewPackagesPage
    success_error_msg = NotificationMessages.NewPackagePage

    def test_validation_of_required_fields_in_new_package_form(self):
        """
        Test Steps:
            1. Click on "New Package" option from side navigation panel
            2. Click on "Create Package" button without filling any details

        Scenario Tested:
        [x] Verify that user should get error messages for required fields in new package form.
        """
        new_package_page = NewPackagesPage(self.driver)
        new_package_page.open(url=BaseConstants.Urls.NEW_PACKAGES_PAGE_URL)
        new_package_page.click(by_locator=self.new_package_locator.create_package_button)

        error_msg_dict = {self.new_package_constant.FULL_NAME: self.success_error_msg.full_name_error_msg,
                          self.new_package_constant.STATUS_FOR_POSTING: self.success_error_msg.pkg_status_error_msg,
                          self.new_package_constant.DATE_RECEIVED: self.success_error_msg.date_received_error_msg,
                          self.new_package_constant.CARRIER: self.success_error_msg.carrier_error_msg,
                          self.new_package_constant.TRACKING_NUMBER: self.success_error_msg.tracking_number_error_msg,
                          self.new_package_constant.VENDOR: self.success_error_msg.vendor_error_msg,
                          self.new_package_constant.WEIGHT: self.success_error_msg.weight_error_msg}

        for required_field in self.new_package_constant.REQUIRED_FIELDS:
            label_element = new_package_page.get_element_of_required_field_label(field_name=required_field)

            assert new_package_page.get_color_code_of_ui_element(
                element=label_element, css_property="color") == BaseConstants.ERROR_COLOR_CODE, \
                "'{}' field does not highlighted with red color after keeping it blank even though it is " \
                "required.".format(required_field)

            assert error_msg_dict[required_field] in new_package_page.get_required_field_error_messages(), \
                "Error message is missing or mismatch for '{}' required field.".format(required_field)

    def test_validation_of_required_fields_in_add_content_modal(self):
        """
        Test Steps:
            1. Click on "New Package" option from side navigation panel
            2. Click on "Add Content" button

        Scenario Tested:
        [x] Verify that "Add" button should be disabled initially.
        [x] Verify that user should get error messages for required fields in add content modal form.
        [x] Verify that "Add" button should get enabled after filling all required field values.
        """
        new_package_page = NewPackagesPage(self.driver)
        new_package_page.open(url=BaseConstants.Urls.NEW_PACKAGES_PAGE_URL)
        new_package_page.click(by_locator=self.new_package_locator.add_content_button)
        new_package_page.wait_for_element(lambda: new_package_page.is_element_enabled(by_locator=Locators.ops_modal),
                                          waiting_for="'Add Content' modal gets displayed")

        new_package_page.click(by_locator=Locators.ops_modal_title)
        add_content_modal_locator = self.new_package_locator.AddContent

        for locator in [add_content_modal_locator.content_quantity, add_content_modal_locator.content_value]:
            new_package_page.enter_text(by_locator=locator, value=Keys.SPACE)

        new_package_page.click(by_locator=Locators.ops_modal_title)
        sleep_execution(5)
        add_content_modal_constant = self.new_package_constant.AddContent

        for required_field in add_content_modal_constant.REQUIRED_FIELDS:
            if required_field in [add_content_modal_constant.QUANTITY, add_content_modal_constant.VALUE]:
                label_element = new_package_page.get_element_of_required_field_label(field_name=required_field)
            else:
                label_element = new_package_page.find_element_by_xpath(
                    locator_value=add_content_modal_locator.content_category_label)

            assert new_package_page.get_color_code_of_ui_element(
                element=label_element, css_property="color") == BaseConstants.ERROR_COLOR_CODE, \
                "'{}' field does not highlighted with red color after keeping it blank even though it is " \
                "required.".format(required_field)

        new_package_page.get_element_of_add_cancel_button_of_add_content_modal(
            element_name=add_content_modal_constant.CANCEL_BUTTON).click()

    @pytest.mark.parametrize('add_pkg_content', [True, False])
    def test_create_new_package_with_valid_details(self, add_pkg_content):
        """
        Test Steps:
            1. Click on "New Package" option from side navigation panel
            2. Fill all required package details
            3. Click on "Create Package" button

        Scenario Tested:
        [x] Verify that user can able to create new package by filling all required package details.
        """
        new_package_page = NewPackagesPage(self.driver)
        new_package_page.open(url=BaseConstants.Urls.NEW_PACKAGES_PAGE_URL)

        status_of_posting = random.sample(self.new_package_constant.PackageStatus.STATUSES_FOR_POSTING, k=1)
        carrier = random.sample(self.new_package_constant.PackageCarrier.CARRIERS, k=1)
        tracking_number = random.randint(100000, 999999)
        vendor = random.sample(self.new_package_constant.PackageVendors.VENDORS, k=1)
        condition = random.sample(self.new_package_constant.PackageCondition.PACKAGE_CONDITIONS, k=1)

        package_details_dict = {"full_name": "Jigna", "package_status": status_of_posting, "carrier": carrier,
                                "received_date": "01/12/2021", "tracking_number": tracking_number, "vendor": vendor,
                                "weight": random.randint(1, 9), "length": random.randint(1, 9),
                                "width": random.randint(1, 9), "height": random.randint(1, 9), "condition": condition}

        if add_pkg_content:
            content_category = random.sample(self.new_package_constant.AddContent.CONTENT_CATEGORY, k=1)
            country_origin = new_package_page.get_random_country_region_name()

            package_content_dict = {"category": content_category, "quantity": random.randint(1, 9),
                                    "value": random.randint(1, 9), "description": content_category,
                                    "country_origin": country_origin}

            package_details_dict["content_info"] = package_content_dict

        new_package_page.fill_new_package_details(**package_details_dict)
        new_package_page.click(by_locator=self.new_package_locator.create_package_button)
        success_notification = Notifications(self.driver).get_notification_message()

        assert success_notification == self.success_error_msg.create_package_success_msg, \
            "Success notification message is missing or mismatched after creating new package."
