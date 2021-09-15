from CrossBorderPickups.cross_border.lib.locators.locators import Locators
from CrossBorderPickups.cross_border.page_objects.BasePage import BasePage


class Notifications(BasePage):
    """ Defines functions to retrieve the success notification message """

    @property
    def success_message(self) -> str:
        """
        Returns success notification message

        :return: notification message
        :rtype: str
        """
        self.wait_for_element(lambda: self.is_element_visible(by_locator=Locators.notification_msg_div),
                              waiting_for="notification message gets populated")

        return self.get_element_text(by_locator=Locators.notification_msg_text)

    def get_notification_message(self) -> str:
        """
        Returns notification message

        :return: notification message
        :rtype: str
        """
        return self.success_message
