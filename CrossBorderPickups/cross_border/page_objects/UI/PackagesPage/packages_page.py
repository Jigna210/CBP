from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from CrossBorderPickups.cross_border.lib.constants.constant import PageConstants
from CrossBorderPickups.cross_border.lib.locators.locators import Locators
from CrossBorderPickups.cross_border.lib.utility.modal import GenericModal
from CrossBorderPickups.cross_border.lib.utility.table import GenericBaseTable
from CrossBorderPickups.cross_border.page_objects.BasePage import BasePage


class PackagesPage(BasePage):
    """ Page Object class for Shipment Page """

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
        field_number_dict = {package_constant.PACKAGE_RECEIVED_DATE: 4,
                             package_constant.PACKAGE_SIZE: 5, package_constant.PACKAGE_TRACKING_NUMBER: 6}

        for field in fields:
            for row in self.rows:
                row_text = row.text.split()

                if row_text[0] == package_id:
                    if field == package_constant.PACKAGE_STATUS:
                        expected_value = " ".join(row_text[1:4])
                    elif field == package_constant.PACKAGE_CARRIER:
                        expected_value = " ".join(row_text[7:9])
                    else:
                        expected_value = field_number_dict[field]

                    package_details[field] = expected_value
                    break

        return package_details

    def get_package_id_of_pending_order_creation(self, package_ids: list) -> list:
        """
        Returns id of those packages whose status has "Pending order creation"

        :param list package_ids: All packages ids
        :return: ids of "Pending order creation" package
        :rtype: list
        """
        pending_order_creation_ids = []
        package_constant = PageConstants.PackagesPage

        for package_id in package_ids:
            package_status = self.get_package_details_by_id(package_id=package_id,
                                                            fields=[package_constant.PACKAGE_STATUS])['Status']
            if package_status == package_constant.PENDING_ORDER_CREATION:
                pending_order_creation_ids.append(package_id)

        return pending_order_creation_ids


class CreateOrderModal(GenericModal, PackagesList):
    """ Page Object class for Create Order Modal """

    billing_info_locators = Locators.PackagesPage.CreateOrder

    def get_element_of_package_receive_radio_button(self, locator_value: str) -> WebElement:
        """
        Returns Web Element of package received methods radio button by using given value

        :param locator_value: UI locator value
        :return: WebElement
        """
        return self.find_element_by_css_selector(locator_value='input[type="radio"][id="{}"]'.format(
            locator_value.lower()))

    def fill_payment_details(self, **kwargs) -> None:
        """
        Fills user's payment info under order details

        :param kwargs: payment info that to be fill
        :return: None
        """
        self.enter_text(by_locator=self.billing_info_locators.email_field, value=kwargs.get("email_id"))
        self.enter_text(by_locator=self.billing_info_locators.name_on_card_field, value=kwargs.get("card_name"))
        self.enter_text(by_locator=self.billing_info_locators.card_number_field, value=kwargs.get("card_number"))
        self.enter_text(by_locator=self.billing_info_locators.exp_month_field, value=kwargs.get("exp_month"))
        self.enter_text(by_locator=self.billing_info_locators.exp_year_field, value=kwargs.get("exp_year"))
        self.enter_text(by_locator=self.billing_info_locators.cvc_field, value=kwargs.get("cvc_number"))

    def fill_billing_address_details(self, **kwargs) -> None:
        """
        Fills user's billing info under order details

        :param kwargs: billing info that to be fill
        :return: None
        """
        self.enter_text(by_locator=self.billing_info_locators.address_field, value=kwargs.get("address"))
        self.enter_text(by_locator=self.billing_info_locators.city_field, value=kwargs.get("city"))
        self.enter_text(by_locator=self.billing_info_locators.state_field, value=kwargs.get("state"))
        self.enter_text(by_locator=self.billing_info_locators.postal_code_field, value=kwargs.get("postal_code"))
        self.select_region_from_drop_down(**kwargs)

    def select_region_from_drop_down(self, **kwargs) -> None:
        """
        Selects region from billing address under order details

        :param kwargs: region that to be select
        :return: None
        """
        expected_region = kwargs.get("region")

        self.click(by_locator=Locators.select_drop_down_arrow)
        self.enter_text(by_locator=Locators.drop_down_search_field, value=expected_region)
        results = self.find_elements_by_css_selector(locator_value=Locators.drop_down_results)

        for result in results:
            if expected_region == result.get_attribute("innerHTML"):
                result.click()
                break

    def fill_order_details(self, **kwargs) -> None:
        """
        Fills order info under create order modal

        :param kwargs: order info that to be filled
        :return: None
        """
        self.click(by_locator=self.get_element_of_package_receive_radio_button(locator_value=kwargs.get(
            "pkg_receive_method")))
        self.fill_payment_details(**kwargs)
        self.fill_billing_address_details(**kwargs)


class AddContentModal(GenericModal, PackagesList):
    """ Page Object class for Add Content Modal """

    add_content_constant = Locators.PackagesPage.AddContent

    def select_duty_category_from_drop_down_item(self, category_value: str) -> None:
        """
        Selects duty category item for given category value in 'Add content' modal

        :param str category_value: category value to be enter
        :return: None
        """
        self.enter_text(by_locator=self.add_content_constant.duty_category_field, value=category_value)
        self.wait_for_element(lambda: self.is_element_visible(
            by_locator=self.add_content_constant.duty_category_list_panel),
                              waiting_for="duty category results get displayed")

        if self.is_element_visible(by_locator=self.add_content_constant.duty_category_list_panel):
            category_items = self.find_elements_by_css_selector(
                locator_value=self.add_content_constant.duty_category_items)

            for category in category_items:
                if category.text == category_value:
                    self.click_element_by_javascript(element=category)
                    break

    def fill_add_content_form(self, **kwargs) -> None:
        """
        Fills package content by using given details in 'Add content' modal

        :param kwargs: package content details that to be fill
        :return: None
        """
        self.select_duty_category_from_drop_down_item(category_value=kwargs.get("duty_category"))
        self.select_country_from_drop_down(country=kwargs.get("country_origin"))
        self.enter_text(by_locator=self.add_content_constant.quantity_field, value=kwargs.get("quantity"))
        self.enter_text(by_locator=self.add_content_constant.value_usd_field, value=kwargs.get("content_value"))
        self.enter_text(by_locator=self.add_content_constant.description_area,
                        value=kwargs.get("content_description"))
        self.click(by_locator=self.add_content_constant.add_button)
