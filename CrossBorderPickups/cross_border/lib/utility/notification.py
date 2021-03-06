from CrossBorderPickups.cross_border.lib.locators.locators import Locators
from CrossBorderPickups.cross_border.page_objects.BasePage import BasePage


class Notifications(BasePage):
    """ Defines functions to retrieve the success notification message """

    notification_locator = Locators.Notification

    @property
    def notification_message(self) -> str:
        """
        Returns success notification message

        :return: notification message
        :rtype: str
        """
        expected_locator = self.notification_locator.ops_notification_msg_text if "-ops-" in self.get_url() else \
            self.notification_locator.notification_msg_text
        self.wait_for_element(lambda: self.is_element_visible(by_locator=expected_locator),
                              waiting_for="notification message gets populated")

        return self.get_element_text(by_locator=expected_locator)

    def get_notification_message(self) -> str:
        """
        Returns notification message

        :return: notification message
        :rtype: str
        """
        return self.notification_message

    def clear_notification(self) -> None:
        """
        Clears notifications

        :return: None
        """
        self.click(by_locator=self.notification_locator.notification_close_button)
