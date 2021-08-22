import os
from subprocess import TimeoutExpired
from urllib.error import URLError

from selenium.common.exceptions import WebDriverException, TimeoutException, UnexpectedAlertPresentException
from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from CrossBorderPickups.cross_border.lib.configs.config import Config
from CrossBorderPickups.cross_border.lib.constants.constant import BaseConstants


class BasePage(object):
    """
    This class is the parent class of all the pages in our application and it contains
    all common elements and functionalities available to all pages.
    """

    def __init__(self, driver):
        self.base_url = BaseConstants.Urls.BASE_URL
        self.driver = driver
        self.driver.implicitly_wait(time_to_wait=BaseConstants.DEFAULT_TIMEOUT)

    def open(self, url: str) -> None:
        """
        Opens the page URL by appending given URL with base URL

        :param str url: page endpoint
        :return: None
        """
        page_url = self.base_url + url if url else self.base_url
        self.driver.get(page_url)

    def find_element(self, by_locator: str) -> WebElement:
        """
        Finds web element on UI page by given locator

        :param str by_locator: UI locator
        :return: Web element of UI locator
        :rtype: WebElement
        """
        return self.driver.find_element(by_locator)

    def find_elements(self, by_locator: str) -> WebElement:
        """
        Finds web elements on UI page by given locator

        :param str by_locator: UI locator
        :return: Web element of UI locator
        :rtype: WebElement
        """
        return self.driver.find_elements(by_locator)

    def click(self, by_locator: str) -> None:
        """
        Clicks on web element located by given locator

        :param str by_locator: UI locator
        :return: None
        """
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        element.click()

    def get_title(self) -> str:
        """
        Returns title of page

        :return: page title
        :rtype: str
        """
        return self.driver.title

    def get_url(self) -> str:
        """
        Returns url of current page

        :return: page url
        :rtype: str
        """
        return self.driver.current_url

    def enter_text(self, by_locator: str, value: str) -> None:
        """
        Enters given text in web element located by given locator

        :param str by_locator: UI locator
        :param str value: value that need to be enter
        :return: None
        """
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(value)

    def get_element_text(self, by_locator: str) -> str:
        """
        Returns text from web element located at given locator

        :param str by_locator: UI locator
        :return: text value from web element
        :rtype: str
        """
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return element.text

    def is_enabled(self, by_locator: str) -> bool:
        """
        Checks that web element located at given locator is enabled

        :param str by_locator: UI locator
        :return: True is web element is enabled else False
        :rtype: bool
        """
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))

    def is_visible(self, by_locator: str) -> bool:
        """
        Checks that web element located at given locator is visible on UI

        :param str by_locator: UI locator
        :return: True is web element is visible on UI else False
        :rtype: bool
        """
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return bool(element)

    def move_to_element(self, by_locator: str) -> None:
        """
        Moves to the web element located at given locator by hovering the mouse

        :param str by_locator: UI locator
        :return: None
        """
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        ActionChains(self.driver).move_to_element(element).perform()

    def take_screenshot(self, filename, path=None) -> str:
        """
        Function to take a screenshot of the current page.

        :param str filename: The absolute path to save the screenshot to.
        :param str path: Path to save file to. Default: output/screenshots.
        :return: None if screenshot was not taken; screenshot path otherwise
        """
        file_path = None

        if path is None:
            path = Config.SCREENSHOTS_DIR
        elif os.path.sep in filename:
            file_path = os.path.normpath(filename)
            path = os.path.normpath(os.path.split(filename)[0])
        else:
            file_path = os.path.normpath(os.path.join(path, filename))

        if self.driver:
            os.makedirs(path, exist_ok=True)

            try:
                self.driver.save_screenshot(file_path)
                return file_path
            except (WebDriverException, URLError):
                print('An unexpected error occurred while attempting to screenshot with the driver.')

    def wait_for_element(self, method, **kwargs) -> None:
        """
        Method to wait for an UI event such as an element to be located.

        Kwargs:
            timeout_seconds (int): Override default timeout of 30 seconds.
            sleep_seconds (float, int): Override default sleep interval between calls. Default 0.5.
            expected_exceptions (list, tuple): Iterable structure of expected exceptions. Default: WebDriverException.
            waiting_for (str): A message describing what we're waiting for.

        :param lambda method: Calls the supplied method until it returns True, if before the timeout occurs.
        :return: None
        :raises: TimeoutExpired
        """
        timeout = kwargs.get('timeout_seconds', BaseConstants.DEFAULT_TIMEOUT)
        poll_frequency = kwargs.get('sleep_seconds', 0.5)
        ignored_exceptions = kwargs.get('expected_exceptions', (WebDriverException,
                                                                UnexpectedAlertPresentException))
        waiting_for = kwargs.get('waiting_for', '')

        try:
            WebDriverWait(self.driver, timeout, poll_frequency, ignored_exceptions).until(lambda x: method())
        except TimeoutException:
            raise TimeoutExpired(timeout, waiting_for)
