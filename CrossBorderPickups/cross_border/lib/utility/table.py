from selenium.common.exceptions import NoSuchElementException

from CrossBorderPickups.cross_border.lib.locators.locators import Locators
from CrossBorderPickups.cross_border.page_objects.BasePage import BasePage


class GenericBaseTable(BasePage):
    """ Defines functions to access table elements like row, columns, etc. """

    @property
    def table_rows(self) -> list:
        """ Accessor for the table_rows in a Generic Table. If there is no table it returns empty list """
        try:
            return self.find_elements_by_css_selector(locator_value=Locators.table_row)
        except NoSuchElementException:
            return []

    @property
    def modal_table_rows(self) -> list:
        """ Accessor for the table_rows in a Generic Table. If there is no table it returns empty list """
        try:
            return self.find_elements_by_css_selector(locator_value=Locators.modal_table_row)
        except NoSuchElementException:
            return []

    def get_content_table_rows(self, package_id: str) -> list:
        """ Accessor for the table_rows in a Generic Table. If there is no table it returns empty list """
        locator = './/input[@id="{}"]//ancestor::tr//following::tr[2]//table[contains(@class, "table-sm")]//' \
                  'tbody//tr'.format(package_id)

        try:
            return self.find_elements_by_xpath(locator_value=locator)
        except NoSuchElementException:
            return []

    @property
    def columns(self) -> list:
        """ Accessor for the columns in a Generic Table. If there is no table it returns empty list """
        try:
            return self.find_elements_by_css_selector(locator_value=Locators.table_column)
        except NoSuchElementException:
            return []
