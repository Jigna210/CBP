from selenium.common.exceptions import NoSuchElementException

from cross_border.lib.constants.constant import BaseConstants
from cross_border.lib.locators.locators import Locators
from cross_border.page_objects.BasePage import BasePage


class GenericBaseTable(BasePage):
    """ Defines functions to access table elements like row, columns, etc. """

    @property
    def rows(self) -> list:
        """ Accessor for the rows in a Generic Table. If there is no table it returns empty list """
        try:
            return self.find_elements_by_css_selector(locator_value=BaseConstants.table_row)
        except NoSuchElementException:
            return []

    @property
    def columns(self) -> list:
        """ Accessor for the columns in a Generic Table. If there is no table it returns empty list """
        try:
            return self.find_elements_by_css_selector(locator_value=BaseConstants.table_column)
        except NoSuchElementException:
            return []
