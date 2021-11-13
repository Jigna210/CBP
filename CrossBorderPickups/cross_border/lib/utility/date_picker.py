import calendar

from CrossBorderPickups.cross_border.lib.locators.locators import Locators
from CrossBorderPickups.cross_border.page_objects.BasePage import BasePage


class GenericDatePicker(BasePage):
    """ Defines functions to select date from date picker """

    def select_date_from_date_picker_calendar(self, calendar_date: str) -> None:
        """
        Selects given date from date picker calendar

        :param str calendar_date: date to be selected
        :return: None
        """
        split_date = calendar_date.split("/")
        expected_date, month_number, expected_year = split_date[0], split_date[1].lstrip("0"), split_date[2]

        self.click(by_locator=Locators.NewPackagesPage.date_picker_toggle_button)
        self.click(by_locator=Locators.NewPackagesPage.month_year_button)

        calendar_year_elements = self.find_elements_by_css_selector(
            locator_value=Locators.NewPackagesPage.calender_body_content)

        while int(expected_year) < int(calendar_year_elements[0].text):
            self.click(by_locator=Locators.NewPackagesPage.previous_year_button)

            calendar_year_elements = self.find_elements_by_css_selector(
                locator_value=Locators.NewPackagesPage.calender_body_content)

        while int(calendar_year_elements[-1].text) < int(expected_year):
            self.click(by_locator=Locators.NewPackagesPage.next_year_button)

            calendar_year_elements = self.find_elements_by_css_selector(
                locator_value=Locators.NewPackagesPage.calender_body_content)

        for value in ["year", "month", "date"]:
            expected_value_dict = {"year": expected_year, "date": expected_date,
                                   "month": calendar.month_name[int(month_number)].upper()[:3]}

            calendar_body_elements = self.find_elements_by_css_selector(
                locator_value=Locators.NewPackagesPage.calender_body_content)

            for calendar_value in calendar_body_elements:
                if calendar_value.text == expected_value_dict[value]:
                    calendar_value.click()
                    break
