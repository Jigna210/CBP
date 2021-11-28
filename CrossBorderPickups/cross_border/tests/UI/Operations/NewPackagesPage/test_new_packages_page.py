import datetime
import random

import pytest
from selenium.webdriver.common.keys import Keys

from CrossBorderPickups.cross_border.lib.constants.constant import BaseConstants, PageConstants
from CrossBorderPickups.cross_border.lib.helpers.helpers import sleep_execution, generate_random_tracking_number
from CrossBorderPickups.cross_border.lib.locators.locators import Locators
from CrossBorderPickups.cross_border.lib.messages.message import NotificationMessages
from CrossBorderPickups.cross_border.lib.utility.notification import Notifications
from CrossBorderPickups.cross_border.page_objects.UI.LoginPage.login_page import LoginPage
from CrossBorderPickups.cross_border.page_objects.UI.Operations.NewPackagesPage.new_packages_page import NewPackagesPage

app_url = BaseConstants.OPERATION_PORTAL_URL
app_user_name = BaseConstants.OPERATION_PORTAL_USERNAME
app_password = BaseConstants.OPERATION_PORTAL_PASSWORD


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
        LoginPage(self.driver).login_in_portal_with_credentials(driver_instance=self.driver, portal_url=app_url,
                                                                user_name=app_user_name, password=app_password)

        new_package_page = NewPackagesPage(self.driver)
        new_package_page.open(url=BaseConstants.Urls.NEW_PACKAGES_PAGE_URL)
        new_package_page.click(by_locator=self.new_package_locator.create_package_button)

        error_msg_dict = {self.new_package_constant.FULL_NAME: self.success_error_msg.full_name_error_msg,
                          self.new_package_constant.STATUS_FOR_POSTING: self.success_error_msg.pkg_status_error_msg,
                          self.new_package_constant.CARRIER: self.success_error_msg.carrier_error_msg,
                          self.new_package_constant.TRACKING_NUMBER: self.success_error_msg.tracking_number_error_msg,
                          self.new_package_constant.VENDOR: self.success_error_msg.vendor_error_msg,
                          self.new_package_constant.WEIGHT: self.success_error_msg.weight_error_msg}

        self.new_package_constant.REQUIRED_FIELDS.remove(self.new_package_constant.DATE_RECEIVED)

        for required_field in self.new_package_constant.REQUIRED_FIELDS:
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
        LoginPage(self.driver).login_in_portal_with_credentials(driver_instance=self.driver, portal_url=app_url,
                                                                user_name=app_user_name, password=app_password)

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

    @pytest.mark.parametrize('add_pkg_content', [False])
    def test_create_new_package_with_valid_details(self, add_pkg_content):
        """
        Test Steps:
            1. Click on "New Package" option from side navigation panel
            2. Fill all required package details
            3. Click on "Create Package" button

        Scenario Tested:
        [x] Verify that user can able to create new package by filling all required package details.
        """
        LoginPage(self.driver).login_in_portal_with_credentials(driver_instance=self.driver, portal_url=app_url,
                                                                user_name=app_user_name, password=app_password)

        new_package_page = NewPackagesPage(self.driver)
        new_package_page.open(url=BaseConstants.Urls.NEW_PACKAGES_PAGE_URL)

        status_of_posting = random.sample(self.new_package_constant.PackageStatus.STATUSES_FOR_POSTING, k=1)[0]
        carrier = random.sample(self.new_package_constant.PackageCarrier.CARRIERS, k=1)[0]
        package_received_date = datetime.date.today().strftime("%d/%m/%Y")
        tracking_number = generate_random_tracking_number()
        vendor = random.sample(self.new_package_constant.PackageVendors.VENDORS, k=1)[0]
        condition = random.sample(self.new_package_constant.PackageCondition.PACKAGE_CONDITIONS, k=1)[0]

        package_details_dict = {"full_name": "Jigna", "status": status_of_posting, "incoming_carrier": carrier,
                                "received_date": package_received_date, "tracking_number": tracking_number,
                                "vendor": vendor, "weight": random.randint(1, 9), "length": random.randint(1, 9),
                                "width": random.randint(1, 9), "height": random.randint(1, 9), "condition": condition}

        new_package_page.fill_package_information(**package_details_dict)

        if add_pkg_content:
            new_package_page.click(by_locator=self.new_package_locator.add_content_button)
            new_package_page.click(by_locator=Locators.ops_modal_title)

            content_category = random.sample(new_package_page.get_auto_suggestion_options(
                field_locator=self.new_package_locator.AddContent.category_or_description), k=1)
            country_origin = new_package_page.get_random_country_region_name()

            package_content_dict = {"category": "Acne patches", "quantity": random.randint(1, 9),
                                    "value": random.randint(1, 9), "description": content_category,
                                    "country_origin": country_origin}

            new_package_page.fill_content_information(**package_content_dict)

        new_package_page.click(by_locator=self.new_package_locator.create_package_button)
        success_notification = Notifications(self.driver).get_notification_message()

        assert success_notification == self.success_error_msg.create_package_success_msg, \
            "Success notification message is missing or mismatched after creating new package."

    def test_verify_date_received_should_not_be_future_date(self):
        """
        Test Steps:
            1. Click on "New Package" option from side navigation panel
            2. Click on date picker icon and wait until it's open

        Scenario Tested:
        [x] Verify that "Date Received" should not be future date under "New Package" tab.
        """
        LoginPage(self.driver).login_in_portal_with_credentials(driver_instance=self.driver, portal_url=app_url,
                                                                user_name=app_user_name, password=app_password)

        new_package_page = NewPackagesPage(self.driver)
        new_package_page.open(url=BaseConstants.Urls.NEW_PACKAGES_PAGE_URL)

        new_package_page.click(by_locator=self.new_package_locator.date_picker_toggle_button)

        assert new_package_page.is_element_visible(by_locator=self.new_package_locator.date_picker_modal), \
            "'Date Picker' modal is not getting displayed after clicking on date picker icon in 'New Package' page."

        today_date = datetime.datetime.now().day
        calendar_body_elements = new_package_page.find_elements_by_css_selector(
            locator_value=self.new_package_locator.calender_body_cell)

        if today_date == calendar_body_elements[-1].text:
            assert not new_package_page.is_element_enabled(by_locator=self.new_package_locator.next_year_button), \
                "Next button icon does not appear disabled even though current date is last date."
        else:
            for date_element in calendar_body_elements[today_date + 1: len(calendar_body_elements)]:
                assert new_package_page.get_attribute_value(by_locator=date_element, attribute_name="aria-disabled"), \
                    "'{}' date does not appear disabled even though it's future date.".format(date_element.text)

        new_package_page.refresh_page()

    def test_package_type_should_display_based_on_weight(self):
        """
        Test Steps:
            1. Click on "New Package" option from side navigation panel
            2. Enter any valid number in "Weight" field

        Scenario Tested:
        [x] Verify that package "Type" should be display based on the weight entered in "Weight" field.
        """
        LoginPage(self.driver).login_in_portal_with_credentials(driver_instance=self.driver, portal_url=app_url,
                                                                user_name=app_user_name, password=app_password)

        new_package_page = NewPackagesPage(self.driver)
        new_package_page.open(url=BaseConstants.Urls.NEW_PACKAGES_PAGE_URL)

        weight_to_be_enter = random.randint(0, 999)
        new_package_page.enter_text(by_locator=self.new_package_locator.weight_field, value=str(weight_to_be_enter))
        new_package_page.wait_for_element(lambda: new_package_page.is_element_visible(
            by_locator=self.new_package_locator.package_type), waiting_for="package type to be visible")

        expected_pkg_type = new_package_page.get_expected_package_type(pkg_weight=weight_to_be_enter)

        assert new_package_page.package_type == expected_pkg_type, \
            "Package type shows incorrect type while entering '{}' weight in 'New Package' page.".format(
                weight_to_be_enter)

    # @pytest.mark.usefixtures("create_new_package")
    # def test_create_new_package_using_fixture(self, create_new_package):
    #     """  """
    #     created_package_details = create_new_package
    #     print(created_package_details)
