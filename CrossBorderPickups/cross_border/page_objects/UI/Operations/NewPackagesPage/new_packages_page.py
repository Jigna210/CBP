from selenium.webdriver.remote.webelement import WebElement

from CrossBorderPickups.cross_border.lib.constants.constant import PageConstants
from CrossBorderPickups.cross_border.lib.locators.locators import Locators
from CrossBorderPickups.cross_border.lib.utility.date_picker import GenericDatePicker
from CrossBorderPickups.cross_border.lib.utility.drop_down import GenericDropDown


class NewPackagesPage(GenericDropDown, GenericDatePicker):
    """ Page Object class for New Packages Page """

    new_package_locator = Locators.NewPackagesPage
    package_type_constant = PageConstants.NewPackagePage.PackageType

    def __init__(self, driver):
        super().__init__(driver)

    @property
    def package_type(self) -> str:
        """ Returns package type """
        return self.get_element_text(by_locator=self.new_package_locator.package_type).strip()

    def fill_package_information(self, **kwargs) -> None:
        """
        Fills package related details into package information section

        :param kwargs: package details to be filled
        :return: None
        """
        package_info_locator = self.new_package_locator

        element_locator_dict = {
            "tracking_number": package_info_locator.tracking_number, "weight": package_info_locator.weight_field,
            "length": package_info_locator.length_field, "width": package_info_locator.width_field,
            "height": package_info_locator.height_field}

        for key in kwargs.keys():
            if key in ["full_name", "status", "incoming_carrier", "condition", "vendor"]:
                field_locator = self.new_package_locator.full_name if key == "full_name" else None
                field_name = None if key == "full_name" else key

                self.select_result_value_from_auto_suggestion_drop_down(
                    field_locator=field_locator, result_locator=Locators.auto_suggestion_results,
                    option_value=kwargs.get(key), field_name=field_name)
            elif key in ["tracking_number", "weight", "length", "width", "height"]:
                self.enter_text(by_locator=element_locator_dict[key], value=kwargs.get(key))
            else:
                self.select_date_from_date_picker_calendar(calendar_date=kwargs.get("received_date"))

    def fill_content_information(self, **kwargs) -> None:
        """
        Fills content related information into "Add Content" modal form

        :param kwargs: content details to be filled
        :return: None
        """
        add_content_locator = self.new_package_locator.AddContent

        element_locator_dict = {
            "category": "category", "quantity": add_content_locator.content_quantity, "country_origin": "coo",
            "value": add_content_locator.content_value, "description": add_content_locator.category_or_description}

        for key in kwargs.keys():
            if key in ["quantity", "value", "description"]:
                self.enter_text(by_locator=element_locator_dict[key], value=kwargs.get(key))
            else:
                field_name = element_locator_dict[key] if key == "category" else None

                self.select_result_value_from_auto_suggestion_drop_down(
                    option_value=kwargs.get(key), field_name=field_name,
                    result_locator=Locators.auto_suggestion_results)

    def fill_additional_fees_information(self, **kwargs) -> None:
        """
        Fills additional fees information into "Additional fees" section

        :param kwargs: additional fees details to be filled
        :return: None
        """
        self.select_result_value_from_auto_suggestion_drop_down(field_name="admin_fee", option_value=kwargs.get(
            "admin_fee"), result_locator=Locators.auto_suggestion_results)
        self.click(by_locator=self.new_package_locator.package_separation_checkbox)

    def get_element_of_required_field_label(self, field_name: str) -> WebElement:
        """
        Returns dynamic web element from UI for given required field

        :param str field_name: required field name
        :return: web element for required field label
        :rtype: WebElement
        """
        locator_value = './/mat-label[contains(@class, "ng-star-inserted") and contains(text(), "{}")]//' \
                        'parent::label'.format(field_name)

        return self.find_element_by_xpath(locator_value=locator_value)

    def get_required_field_error_messages(self) -> list:
        """
        Returns error messages of required field

        :return: error messages
        :rtype: list
        """
        error_msg_elements = self.find_elements_by_css_selector(
            locator_value=self.new_package_locator.required_field_error_msgs)

        return [error.text for error in error_msg_elements]

    def get_element_of_add_cancel_button_of_add_content_modal(self, element_name: str) -> WebElement:
        """
        Returns dynamic web element of "Add" or "Cancel" buttons from "Add Content" modal

        :param str element_name: element name
        :return: web element for given element name
        :rtype: WebElement
        """
        locator_value = './/mat-dialog-actions//span[@class="mat-button-wrapper" and contains(text(), "{}")]'.format(
            element_name)

        return self.find_element_by_xpath(locator_value=locator_value)

    def get_expected_package_type(self, pkg_weight: int) -> str:
        """
        Returns expected package type based on package weight

        :param int pkg_weight: package weight
        :return: expected package type
        :rtype: str
        """
        if pkg_weight <= 1:
            pkg_type = self.package_type_constant.LIGHT
        elif 1 < pkg_weight <= 10:
            pkg_type = self.package_type_constant.REGULAR
        elif 10 < pkg_weight <= 30:
            pkg_type = self.package_type_constant.LARGE
        elif 30 < pkg_weight <= 100:
            pkg_type = self.package_type_constant.OVERSIZE
        else:
            pkg_type = self.package_type_constant.SKID

        return pkg_type
