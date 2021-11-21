import random

from selenium.webdriver.remote.webelement import WebElement

from CrossBorderPickups.cross_border.lib.helpers.helpers import sleep_execution
from CrossBorderPickups.cross_border.lib.locators.locators import Locators
from CrossBorderPickups.cross_border.page_objects.BasePage import BasePage


class GenericDropDown(BasePage):
    """ Defines functions to select elements from drop-down options """

    def click_on_drop_down_arrow(self, field_name: str) -> None:
        """
        Click on given drop-down field arrow

        :param str field_name: dropdown field name
        :return: None
        """
        locator_value = 'mat-select[formcontrolname="{}"] div[class*="mat-select-arrow-wrapper"]'.format(field_name)

        self.find_element_by_css_selector(locator_value=locator_value).click()

    def select_value_from_drop_down_results(self, option_value: str):
        """
        Selects country origin of given country name from country origin list

        :param str option_value: country origin value to be select
        :return: None
        """
        self.click(by_locator=Locators.select_drop_down_arrow)
        self.wait_for_element(lambda: self.is_element_visible(by_locator=Locators.drop_down_search_field),
                              waiting_for="country origin list gets open")

        self.enter_text(by_locator=Locators.drop_down_search_field, value=option_value)
        self.wait_for_element(lambda: self.is_element_visible(by_locator=Locators.country_origin_list_panel),
                              waiting_for="country origin results get displayed")

        if self.is_element_visible(by_locator=Locators.country_origin_list_panel):
            search_results = self.find_elements_by_css_selector(locator_value=Locators.drop_down_results)

            for result in search_results:
                if result.get_attribute("innerHTML").casefold() == option_value.casefold():
                    self.click_element_by_javascript(element=result)
                    break

    def get_all_values_from_drop_down_options(self) -> list:
        """
        Returns all available country or region names from drop-down modal

        :return: name of all available country or region
        :rtype: list
        """
        operation_portal = "-ops-" in self.get_url()
        expected_arrow_locator = Locators.NewPackagesPage.AddContent.country_origin_drop_down_arrow \
            if operation_portal else Locators.select_drop_down_arrow

        self.click(by_locator=expected_arrow_locator)

        if operation_portal:
            sleep_execution(2)
        else:
            self.wait_for_element(lambda: self.is_element_visible(by_locator=Locators.drop_down_search_field),
                                  waiting_for="country origin list gets open")

        expected_result_locator = Locators.auto_suggestion_results if operation_portal else Locators.drop_down_results
        list_of_countries = self.find_elements_by_css_selector(locator_value=expected_result_locator)

        if not operation_portal:
            self.click(by_locator=Locators.select_drop_down_arrow)

        return [option.get_attribute("innerHTML").strip() for option in list_of_countries]

    def select_result_value_from_auto_suggestion_drop_down(
            self, option_value: str, result_locator: str, field_locator: WebElement = None,
            field_name: str = None) -> None:
        """
        Selects given option value from auto suggestion dropdown results

        :param str field_name: drop-down field name
        :param WebElement field_locator: drop-down field element locator
        :param str result_locator: auto-suggestion result elements locator
        :param str option_value: option value to be selected
        :return: None
        """
        new_pkg_locator = Locators.NewPackagesPage

        if field_name:
            if field_name in ["vendor", "category"]:
                field_locator_dict = {"vendor": new_pkg_locator.vendor_dropdown,
                                      "category": new_pkg_locator.AddContent.category_or_description}

                self.click(by_locator=field_locator_dict[field_name])
            else:
                self.click_on_drop_down_arrow(field_name=field_name)
        else:
            self.enter_text(by_locator=field_locator, value=option_value)

        sleep_execution(time_seconds=3)
        auto_suggestion_results = self.find_elements_by_css_selector(locator_value=result_locator)

        for result_option in auto_suggestion_results:
            if option_value in result_option.text:
                result_option.click()
                break

    def get_random_country_region_name(self) -> str:
        """
        Return random country or region name from available country names

        :return: country or region name
        :rtype: str
        """
        return random.sample(self.get_all_values_from_drop_down_options(), k=1)[0]

    def get_auto_suggestion_options(self, field_locator: WebElement) -> list:
        """
        Returns list of options from auto suggestion drop-down

        :param WebElement field_locator: drop-down field element locator
        :return: list of auto suggestion options
        :rtype: list
        """
        self.click(by_locator=field_locator)
        sleep_execution(time_seconds=3)
        auto_suggestion_results = self.find_elements_by_css_selector(locator_value=Locators.auto_suggestion_results)

        return [result.text for result in auto_suggestion_results]
