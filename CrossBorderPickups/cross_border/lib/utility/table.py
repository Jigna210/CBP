from selenium.common.exceptions import NoSuchElementException

from CrossBorderPickups.cross_border.lib.locators.locators import Locators
from CrossBorderPickups.cross_border.page_objects.BasePage import BasePage


class GenericBaseTable(BasePage):
    """ Defines functions to access table elements like row, columns, etc. """

    @property
    def table_rows(self) -> list:
        """ Returns list of web elements of table rows """
        try:
            return self.find_elements_by_css_selector(locator_value=Locators.table_row)
        except NoSuchElementException:
            return []

    @property
    def modal_table_rows(self) -> list:
        """ Returns list of web elements of table rows under modal """
        try:
            return self.find_elements_by_css_selector(locator_value=Locators.modal_table_row)
        except NoSuchElementException:
            return []

    def get_content_table_rows(self, package_id: str) -> list:
        """ Returns list of web elements of table rows content """
        locator = './/input[@id="{}"]//ancestor::tr//following::tr[2]//table[contains(@class, "table-sm")]//' \
                  'tbody//tr'.format(package_id)

        try:
            return self.find_elements_by_xpath(locator_value=locator)
        except NoSuchElementException:
            return []

    @property
    def columns(self) -> list:
        """ Returns list of web elements of table columns """
        try:
            return self.find_elements_by_css_selector(locator_value=Locators.table_column)
        except NoSuchElementException:
            return []

    def click_on_row(self, row_to_be_select: str) -> None:
        """ Clicks on table row of given row """
        for row in self.table_rows:
            table_data = row.find_elements_by_tag_name("td")

            if table_data[1].text == row_to_be_select:
                row.click()
                break
