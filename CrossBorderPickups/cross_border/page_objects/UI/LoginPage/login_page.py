from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from CrossBorderPickups.cross_border.lib.configs.environmental_variables import CBP
from CrossBorderPickups.cross_border.lib.locators.locators import Locators
from CrossBorderPickups.cross_border.page_objects.BasePage import BasePage


class LoginPage(BasePage):
    """ Page Object for Login Page """

    def __init__(self, driver):
        super().__init__(driver)

    def login_with_defaults(self) -> None:
        """
        Automatically login using default configured username and password

        :return: None
        """
        # self._do_login(BaseConstants.CUSTOMER_USER_NAME, BaseConstants.DEFAULT_PASSWORD)
        self._do_login(CBP.CBP_USERNAME, CBP.CBP_PASSWORD)

    def login_with_credentials(self, username: str, password: str) -> None:
        """
        Login into product using specified credentials.

        :param str username: The account username.
        :param str password: The account password.
        """
        self._do_login(username, password)

    def _do_login(self, username: str, password: str) -> None:
        """
        Login into product by entering username and password and click on login button

        :param str username: Username or email id
        :param str password: password
        :return: None
        """
        self.enter_text(by_locator=Locators.LoginPage.email_id, value=username)
        self.enter_text(by_locator=Locators.LoginPage.password, value=password)
        self.click(by_locator=Locators.LoginPage.login_button)

    def do_login(self) -> None:
        """
        Helper function to perform login to Product

        :return: None
        """
        self.login_with_defaults()

    def do_logout(self) -> None:
        """
        Function for logout from Application
        """
        self.click(by_locator=Locators.LoginPage.user_icon)
        self.click(by_locator=Locators.LoginPage.logout_button)
        
    def login_in_portal_with_credentials(self, driver_instance, portal_url: str, user_name: str, password: str) -> None:
        """
        Helper function to login into given portal URL with given username and password

        :param driver_instance: driver instance
        :param str portal_url: URL of application in which user to be login
        :param str user_name: user name to get login into application
        :param str password: password to get login into application
        :return: None
        """
        driver_instance.get(url=portal_url)
        self.login_with_credentials(username=user_name, password=password)

        expected_locator = Locators.HeaderPage.operation_button if "-ops-" in driver_instance.current_url else \
            Locators.HeaderPage.user_avatar
        self.wait_for_element(lambda: WebDriverWait(driver_instance, 10).until(EC.visibility_of_element_located(
            expected_locator)), waiting_for="dashboard gets displayed after login")

    def do_user_can_sign_up_personal_account(self) -> None:
        """
        Function for user do Sign-Up successfully in application.
        """
        self.click(by_locator=Locators.SignUpPage.sign_up_link)
        self.click(by_locator=Locators.SignUpPage.personal_account)
        self.enter_text(by_locator=Locators.PersonSignUp.fullname, value="test")
        self.enter_text(by_locator=Locators.PersonSignUp.email, value="test@cbp.in")
        self.enter_text(by_locator=Locators.PersonSignUp.password, value="123456")
        self.enter_text(by_locator=Locators.PersonSignUp.confirmPassword, value="123456")
        self.enter_text(by_locator=Locators.PersonSignUp.line1, value="address1")
        self.enter_text(by_locator=Locators.PersonSignUp.line2, value="address2")
        self.enter_text(by_locator=Locators.PersonSignUp.city, value="ON")
        self.select_from_drop_down(by_locator=Locators.PersonSignUp.province, value='Alberta')
        self.enter_text(by_locator=Locators.PersonSignUp.postal_code, value="MG1 012")
