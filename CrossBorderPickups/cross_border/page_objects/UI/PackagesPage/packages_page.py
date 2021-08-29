from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from CrossBorderPickups.cross_border.lib.constants.constant import PageConstants
from CrossBorderPickups.cross_border.lib.locators.locators import Locators
from CrossBorderPickups.cross_border.lib.utility.modal import GenericModal
from CrossBorderPickups.cross_border.lib.utility.table import GenericBaseTable
from CrossBorderPickups.cross_border.page_objects.BasePage import BasePage


class PackagesPage(BasePage):
    """ Page Object for Shipment Page """

    def __init__(self, driver):
        super().__init__(driver)


class PackagesList(GenericBaseTable):
    """ Defines functions for Packages records displayed in packages list table """

    def get_element_of_package_checkbox(self, package_id: str, element_on_modal: bool = False) -> WebElement:
        """
        Returns dynamic web element of checkbox for given package id

        :param str package_id: Id of package that to be selected
        :param bool element_on_modal: True if web element on modal else False
        :return: Web Element of checkbox
        :rtype: WebElement
        """
        expected_pid = "order-{}".format(package_id) if element_on_modal else package_id

        element = self.find_element_by_xpath(
            locator_value='.//input[@class="custom-control-input" and @id="{}"]'.format(expected_pid))

        return element

    def get_element_of_content_block_title(self, package_id: str):
        """
        Returns dynamic web element of content block header

        :param str package_id: Id of package that to be selected
        :return: Web Element of package content title
        :rtype: WebElement
        """
        element = self.find_element_by_xpath(
            locator_value='.//input[@id="{}"]//ancestor::tr//following::tr//h4[contains('
                          '@class, "header-title")]'.format(package_id))

        return element

    def get_element_of_package_content_table(self, package_id: str):
        """
        Returns dynamic web element of package content table

        :param str package_id: Id of package that to be selected
        :return: Web Element of package content table
        :rtype: WebElement
        """
        element = self.find_element_by_xpath(
            locator_value='.//input[@id="{}"]//ancestor::tr//following::tr//table'.format(package_id))

        return element

    def get_all_packages_id(self) -> list:
        """
        Returns all available packages id from package list table

        :return: packages ids
        :rtype: list
        """
        return [row.text.split()[0] for row in self.rows]

    def select_package_by_id(self, package_id: str, element_on_modal: bool = False) -> None:
        """
        Selects the checkbox from package list table for given package id

        :param str package_id: Id of package that to be selected
        :param bool element_on_modal: True if web element on modal else False
        :return: None
        """
        web_element = self.get_element_of_package_checkbox(package_id=package_id, element_on_modal=element_on_modal)
        self.click_element_by_javascript(element=web_element)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_selected(element=web_element))

    def get_package_details_by_id(self, package_id: str, fields: list) -> dict:
        """
        Returns package details for given fields from package list table

        :param str package_id: Id of package that details to be want
        :param fields: package field that to be want like status, size, tracking number, etc...
        :return: package details of given package id
        :rtype: dict
        """
        package_details = {}

        package_constant = PageConstants.PackagesPage
        field_number_dict = {package_constant.PACKAGE_STATUS: 1, package_constant.PACKAGE_RECEIVED_DATE: 2,
                             package_constant.PACKAGE_SIZE: 3, package_constant.PACKAGE_TRACKING_NUMBER: 4,
                             package_constant.PACKAGE_CARRIER: 5}

        package_info = self.get_all_packages_id()

        for field in fields:
            for info in package_info:
                row_text = info.text.split()

                if row_text[0] == package_id:
                    package_details[field] = row_text[field_number_dict[field]]

        return package_details


class CreateOrderModal(GenericModal, PackagesList):
    """ Page Object for Create Order Modal """

    def select_package_received_method(self, locator_value: str) -> None:
        """
        Select package received radio button by using given value

        :param locator_value: UI locator value
        :return: None
        """
        element = self.find_element_by_id(locator_value=locator_value.lower())
        element.click()

    def fill_payment_details(self, **kwargs) -> None:
        """
        Fills user's payment info under order details

        :param kwargs: payment info that to be fill
        :return: None
        """
        payment_info_locators = Locators.PackagesPage.CreateOrder

        self.enter_text(by_locator=payment_info_locators.email_field, value=kwargs.get(k="email_id"))
        self.enter_text(by_locator=payment_info_locators.name_on_card_field, value=kwargs.get(k="card_name"))
        self.enter_text(by_locator=payment_info_locators.card_number_field, value=kwargs.get(k="card_number"))
        self.enter_text(by_locator=payment_info_locators.exp_month_field, value=kwargs.get(k="exp_month"))
        self.enter_text(by_locator=payment_info_locators.exp_year_field, value=kwargs.get(k="exp_year"))
        self.enter_text(by_locator=payment_info_locators.cvc_field, value=kwargs.get(k="cvc_number"))

    def fill_billing_address_details(self, **kwargs) -> None:
        """
        Fills user's billing info under order details

        :param kwargs: billing info that to be fill
        :return: None
        """
        payment_info_locators = Locators.PackagesPage.CreateOrder

        self.enter_text(by_locator=payment_info_locators.address_field, value=kwargs.get(k="address"))
        self.enter_text(by_locator=payment_info_locators.city_field, value=kwargs.get(k="city"))
        self.enter_text(by_locator=payment_info_locators.state_field, value=kwargs.get(k="state"))
        self.enter_text(by_locator=payment_info_locators.postal_code_field, value=kwargs.get(k="postal_code"))
        self.select_region_from_drop_down(**kwargs)

    def select_region_from_drop_down(self, **kwargs) -> None:
        """
        Selects region from billing address under order details

        :param kwargs: region that to be select
        :return: None
        """
        payment_info_locators = Locators.PackagesPage.CreateOrder
        expected_region = kwargs.get(k="region")

        self.click(by_locator=payment_info_locators.region_selection_arrow)
        self.enter_text(by_locator=payment_info_locators.region_text_field, value=expected_region)
        results = self.find_elements(by_locator=payment_info_locators.region_results)

        for result in results:
            if expected_region in result.text:
                result.click()

    def fill_order_details(self, **kwargs) -> None:
        """
        Fills order info under create order modal

        :param kwargs: order info that to be filled
        :return: None
        """
        self.select_package_received_method(kwargs.get(k="pkg_receive_method"))
        self.fill_payment_details(**kwargs)
        self.fill_billing_address_details(**kwargs)
