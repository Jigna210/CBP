from selenium.webdriver.remote.webelement import WebElement

from CrossBorderPickups.cross_border.lib.configs.environmental_variables import CBP
from CrossBorderPickups.cross_border.page_objects.BasePage import BasePage


class SideNavigation(BasePage):
    """ Defines functions to access side navigation options """

    def get_element_of_side_navigation_option(self, sub_menu: str, menu: str = None) -> WebElement:
        """
        Returns dynamic web element for given side navigation option

        :param str menu: side navigation main menu
        :param str sub_menu: side navigation sub menu
        :return: dynamic web element of side navigation option
        :rtype: WebElement
        """
        ops_locator = './/mat-list-item//div[contains(text(), "{}")]'.format(sub_menu)
        locator = './/li[contains(@class, "side-nav-item") and contains(text(), "{}")]//following-sibling::li//span[' \
                  'contains(text(), "{}")]'.format(menu, sub_menu)
        expected_locator = ops_locator if "-ops-" in CBP.APPLICATION_URL else locator

        return self.find_element_by_xpath(locator_value=expected_locator)
