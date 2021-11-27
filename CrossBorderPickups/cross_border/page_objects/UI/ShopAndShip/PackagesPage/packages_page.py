import random
import string
from datetime import date

from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from CrossBorderPickups.cross_border.lib.constants.constant import PageConstants, BaseConstants
from CrossBorderPickups.cross_border.lib.locators.locators import Locators
from CrossBorderPickups.cross_border.lib.utility.drop_down import GenericDropDown
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

    def get_element_of_content_block_title(self, package_id: str) -> WebElement:
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

    def get_element_of_package_content_table(self, package_id: str) -> WebElement:
        """
        Returns dynamic web element of package content table

        :param str package_id: Id of package that to be selected
        :return: Web Element of package content table
        :rtype: WebElement
        """
        element = self.find_element_by_xpath(
            locator_value='.//input[@id="{}"]//ancestor::tr//following::tr//table'.format(package_id))

        return element

    def get_all_packages_id(self, table_on_modal: bool = False) -> list:
        """
        Returns all available packages id from package list table

        :param bool table_on_modal: True if web table on modal else False
        :return: packages ids
        :rtype: list
        """
        all_rows = self.modal_table_rows if table_on_modal else self.table_rows

        return [row.text.split()[0].split("\n")[0] for row in all_rows]

    def get_package_id_from_other_field_value(self, package_header: str, values: list) -> list:
        """
        Returns all available packages id from package list table

        :param str package_header: packages list table header like "Package Id", "Status", etc...
        :param list values: value from given package header rows
        :return: list of packages id
        :rtype: list
        """
        package_ids = []
        package_header_index_dict = {"Package Id": 1, "Status": 2, "Received": 3, "Received From": 4, "Size": 5,
                                     "Incoming Carrier Tracking Number": 6, "Incoming Carrier": 7}

        for value in values:
            for row in self.table_rows:
                if value == row.find_elements_by_tag_name("td")[package_header_index_dict[package_header]].text:
                    package_ids.append(row.find_elements_by_tag_name("td")[1].text)

        return package_ids

    def select_package_by_id(self, package_id: str, element_on_modal: bool = False, is_select: bool = True) -> None:
        """
        Selects the checkbox from package list table for given package id

        :param str package_id: Id of package that to be selected
        :param bool element_on_modal: True if web element on modal else False
        :param bool is_select: True if checkbox to be selected else False to deselect
        :return: None
        """
        web_element = self.get_element_of_package_checkbox(package_id=package_id, element_on_modal=element_on_modal)
        self.click_element_by_javascript(element=web_element)

        if is_select:
            WebDriverWait(self.driver, 10).until(EC.element_to_be_selected(element=web_element))

    def get_package_details_by_id(self, package_id: str, fields: list) -> dict:
        """
        Returns package details for given fields from package list table

        :param str package_id: Id of package that details to be want
        :param list fields: package field that to be want like status, size, tracking number, etc...
        :return: package details of given package id
        :rtype: dict
        """
        package_details = {}
        package_constant = PageConstants.PackagesPage
        package_header_index_dict = {
            package_constant.PACKAGE_ID: 1, package_constant.PACKAGE_STATUS: 2, package_constant.PACKAGE_RECEIVED: 3,
            package_constant.PACKAGE_RECEIVED_FROM: 4, package_constant.PACKAGE_SIZE: 5,
            package_constant.PACKAGE_TRACKING_NUMBER: 6, package_constant.PACKAGE_CARRIER: 7}

        for field in fields:
            for row in self.table_rows:
                table_data = row.find_elements_by_tag_name("td")

                if table_data[1].text == package_id:
                    package_details[field] = table_data[package_header_index_dict[field]].text
                    break

        return package_details

    def get_element_of_content_edit_delete_icon(self, package_id: str, category: str, locator_value: str) -> WebElement:
        """
        Returns dynamic web element of package content table

        :param str package_id: Id of package that to be selected
        :param str category: content category that to be edited
        :param str locator_value: locator value of edit/delete icon
        :return: Web Element of edit content icon from package content table
        :rtype: WebElement
        """
        element = self.find_element_by_xpath(
            locator_value='.//input[@id="{}"]//ancestor::tr//following::tr[2]//td[contains(text(), "{}")]//'
                          'following::td[7]//i[contains(@class, "{}")]'.format(package_id, category, locator_value))

        return element

    def get_categories_from_package_content_table(self, package_id: str) -> list:
        """
        Returns available packages category from package content table

        :param str package_id: Id of package that content to be edited
        :return: packages categories
        :rtype: list
        """
        rows = self.get_content_table_rows(package_id=package_id)

        return [row.text.split()[0] for row in rows]

    def get_package_content_table_details_by_category(self, package_id: str, category: str, fields: list) -> dict:
        """
        Returns package details for given fields from package list table

        :param str package_id: Id of package that content to be selected
        :param str category: category of package content that details to be want
        :param list fields: package content field that to be want like Qty, Value, Duties, Tax...
        :return: package content details of given content category
        :rtype: dict
        """
        content_details = {}
        content_constant = PageConstants.PackagesPage.AddContent
        rows = self.get_content_table_rows(package_id=package_id)

        field_number_dict = {
            content_constant.CONTENT_QTY: 1, content_constant.CONTENT_VALUE: 2, content_constant.CONTENT_TOTAL_VALUE: 3,
            content_constant.CONTENT_TOTAL_VALUE_CAD: 4, content_constant.CONTENT_EST_DUTIES: 5,
            content_constant.CONTENT_EST_TAX: 6}

        for field in fields:
            for row in rows:
                row_text = row.text.split()

                if row_text[0] == category:
                    content_details[field] = field_number_dict[field]
                    break

        return content_details


class CreateOrderDropDown(GenericDropDown, PackagesList):
    """ Page Object class for Create Order Modal """

    create_order_locators = Locators.PackagesPage.CreateOrder
    create_order_constants = PageConstants.PackagesPage.CreateOrder

    def get_element_of_package_receive_radio_button(self, locator_value: str) -> WebElement:
        """
        Returns Web Element of package received methods radio button by using given value

        :param locator_value: UI locator value
        :return: WebElement
        """
        return self.find_element_by_css_selector(locator_value='input[id="{}"]'.format(locator_value.lower()))

    def fill_payment_details(self, **kwargs) -> None:
        """
        Fills user's payment info under order details

        :param kwargs: payment info that to be fill
        :return: None
        """
        payment_locator = self.create_order_locators

        payment_details_dict = {
            "email_id": payment_locator.email_field, "cvc_number": payment_locator.cvc_field,
            "card_name": payment_locator.name_on_card_field, "exp_year": payment_locator.exp_year_field,
            "card_number": payment_locator.card_number_field, "exp_month": payment_locator.exp_month_field}

        for key_data in list(payment_details_dict.keys()):
            self.enter_text(by_locator=payment_details_dict[key_data], value=kwargs.get(key_data))

    def select_region_from_drop_down(self, region_to_select: str) -> None:
        """
        Selects region from billing address under order details

        :param region_to_select: region that to be select
        :return: None
        """
        self.click(by_locator=Locators.select_drop_down_arrow)
        self.enter_text(by_locator=Locators.drop_down_search_field, value=region_to_select)
        results = self.find_elements_by_css_selector(locator_value=Locators.drop_down_results)

        for result in results:
            if region_to_select == result.get_attribute("innerHTML"):
                result.click()
                break

    def fill_shipping_address_details(self, **kwargs) -> None:
        """
        Fills shipping address info under order details

        :param kwargs: shipping address info that to be fill
        :return: None
        """
        shipping_address_dict = {"shipping_name": self.create_order_locators.shipping_address_name,
                                 "shipping_address": self.create_order_locators.select_mail_address}

        for key_data in list(shipping_address_dict.keys()):
            if key_data == "shipping_name":
                self.enter_text(by_locator=shipping_address_dict[key_data], value=kwargs.get(key_data))
            else:
                select_address_element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
                    shipping_address_dict[key_data]))

                select_address = Select(select_address_element)
                select_address.select_by_visible_text(text=kwargs.get(key_data))

    def fill_billing_address_details(self, **kwargs) -> None:
        """
        Fills user's billing info under order details

        :param kwargs: billing info that to be fill
        :return: None
        """
        billing_locator = self.create_order_locators

        billing_address_dict = {"address": billing_locator.address_field, "state": billing_locator.province_field,
                                "city": billing_locator.city_field, "postal_code": billing_locator.postal_code_field}

        for key_data in list(billing_address_dict.keys()):
            self.enter_text(by_locator=billing_address_dict[key_data], value=kwargs.get(key_data))

        self.select_value_from_drop_down_results(option_value=kwargs.get("country"))

    def fill_order_details(self, **kwargs) -> None:
        """
        Fills order info under create order modal

        :param kwargs: order info that to be filled
        :return: None
        """
        if kwargs.get("pkg_receive_method") == self.create_order_constants.PACKAGE_RECEIVE_BY_MAIL:
            self.fill_shipping_address_details(**kwargs)
        else:
            self.click(by_locator=self.get_element_of_package_receive_radio_button(locator_value=kwargs.get(
                "pickup_location")))
            self.fill_billing_address_details(**kwargs)

        self.fill_payment_details(**kwargs)

    def create_billing_and_payment_info_dict(self, shipping_method: str, is_same_address: bool = True) -> dict:
        """
        Returns shipping, billing related required info

        :param str shipping_method: package shipment method
        :param str is_same_address: True if billing and shipping address is same else False
        :return: required billing info
        :rtype: dict
        """
        user_name = "Jiang Chad"
        current_year = date.today().year
        user_email = "{}{}{}@gmail.com".format(''.join(
            random.choice(string.ascii_letters) for _ in range(8)), random.choice("!#$%&*+-/?^_"), ''.join(
            random.choice(string.digits) for _ in range(5)))

        card_number = random.sample(self.create_order_constants.PAYMENT_CARD_NUMBERS, k=1)[0]
        exp_month = random.sample([m for m in range(1, 13)], k=1)[0]
        exp_year = random.sample([y for y in range(current_year + 1, current_year + 6)], k=1)[0]
        cvc_number = random.randint(100, 999)

        postal_code = random.sample(PageConstants.PackagesPage.POSTAL_CODES, k=1)[0]
        city = random.sample(PageConstants.PackagesPage.CANADIAN_CITIES, k=1)[0]
        province = random.sample(PageConstants.PackagesPage.CANADIAN_PROVINCES, k=1)[0]
        country_or_region = self.get_random_country_region_name()

        if shipping_method == self.create_order_constants.PACKAGE_RECEIVE_BY_MAIL and not is_same_address:
            self.click(by_locator=self.create_order_locators.same_billing_address_checkbox)

            address_dict = {'shipping_name': user_name, 'address_line_1': '', 'address_line_2': '',
                            'shipping_city': city, 'shipping_postal_code': postal_code, 'shipping_province': province,
                            'shipping_country': country_or_region}
        else:
            address_dict = {'email_id': user_email, 'address': '', 'city': city, 'state': province,
                            'postal_code': postal_code, 'country': country_or_region}

        order_details_dict = {'pkg_receive_method': shipping_method, 'email_id': user_email,
                              'card_name': user_name, 'card_number': card_number, 'exp_month': exp_month,
                              'exp_year': exp_year, 'cvc_number': cvc_number}

        order_details_dict.update(address_dict)

        return order_details_dict


class AddContentDropDown(GenericDropDown, PackagesList):
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

    def fill_add_content_form(self, edit_content: bool = False, **kwargs) -> None:
        """
        Fills package content by using given details in 'Add content' modal

        :param bool edit_content: True if want to edit content else False to add new content
        :param kwargs: package content details that to be fill
        :return: None
        """
        if not edit_content:
            self.select_duty_category_from_drop_down_item(category_value=kwargs.get("duty_category"))

        self.select_value_from_drop_down_results(option_value=kwargs.get("country_origin"))

        add_content_dict = {'quantity': self.add_content_constant.quantity_field,
                            'content_value': self.add_content_constant.value_usd_field,
                            'content_description': self.add_content_constant.description_area}

        for key_data in list(add_content_dict.keys()):
            self.enter_text(by_locator=add_content_dict[key_data], value=kwargs.get(key_data))

        expected_locator = self.add_content_constant.update_button if edit_content else \
            self.add_content_constant.add_button
        self.click(by_locator=expected_locator)


class DiscardPackagesDropDown(GenericDropDown, PackagesList):
    """ Page Object class for Discard Packages Modal """

    discard_packages_constant = PageConstants.PackagesPage.DiscardPackages

    def get_element_of_discard_package_count_and_total_charge_value(self, element_for: str) -> WebElement:
        """
        Returns Web Element from discard details table from given name of element

        :param element_for: Name of element you want
        :return: WebElement
        """
        discard_details_dict = {self.discard_packages_constant.NUMBER_OF_DISCARDS: 1,
                                self.discard_packages_constant.TOTAL_CHARGE: 2}

        return self.find_element_by_xpath(locator_value='.//div[contains(@class, "active")]//table[contains('
                                                        '@class, "table-bordered")]//tbody//tr[{}]//td[2]'.
                                          format(discard_details_dict[element_for]))

    @staticmethod
    def get_expected_total_charge(discard_package_count: int) -> int:
        """
        Returns total charge of discarded package from given discard package count

        :param int discard_package_count: number of package to be discarded
        :return: total charge on discarded packages
        :rtype: int
        """
        return discard_package_count * BaseConstants.DISCARD_CHARGE_PER_PACKAGE

    def fill_discard_details(self, **kwargs) -> None:
        """
        Fills discard details info under Discard packages modal

        :param kwargs: discard details that to be filled
        :return: None
        """
        create_order_modal = CreateOrderDropDown(self.driver)
        create_order_modal.fill_billing_address_details(**kwargs)
        create_order_modal.fill_payment_details(**kwargs)
