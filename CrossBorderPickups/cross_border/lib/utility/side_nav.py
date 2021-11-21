from selenium.webdriver.remote.webelement import WebElement

from CrossBorderPickups.cross_border.page_objects.BasePage import BasePage


class SideNavigation(BasePage):
    """ Defines functions to access side navigation options """

    def get_element_of_side_nav_panel(self, menu: str) -> WebElement:
        """
        Returns dynamic web element for given side navigation panel

        :param str menu: side navigation main menu name
        :return: dynamic web element of side navigation panel
        :rtype: WebElement
        """
        ops_locator = './/h3[contains(text(), "{}")]'.format(menu)
        locator = './/li[contains(@class, "side-nav-item") and contains(text(), "{}")]'.format(menu)

        expected_locator = ops_locator if "-ops-" in self.get_url() else locator

        return self.find_element_by_xpath(locator_value=expected_locator)

    def get_element_of_side_nav_option(self, menu: str, sub_menu: str) -> WebElement:
        """
        Returns dynamic web element for given side navigation option

        :param str menu: side navigation main menu name
        :param str sub_menu: side navigation sub menu name
        :return: dynamic web element of side navigation option
        :rtype: WebElement
        """
        ops_locator = './/h3[contains(text(), "{}")]//following-sibling::mat-nav-list//div[' \
                      '@class="mat-list-item-content" and contains(text(), "{}")]'.format(menu, sub_menu)

        locator = './/li[contains(@class, "side-nav-item") and contains(text(), "{}")]//following-sibling::li//span[' \
                  'contains(text(), "{}")]'.format(menu, sub_menu)

        expected_locator = ops_locator if "-ops-" in self.get_url() else locator

        return self.find_element_by_xpath(locator_value=expected_locator)
