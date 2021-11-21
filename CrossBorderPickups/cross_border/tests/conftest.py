import os
import platform

import pytest
from _pytest.fixtures import SubRequest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from CrossBorderPickups.cross_border.lib.configs import config
from CrossBorderPickups.cross_border.lib.constants.constant import BaseConstants
from CrossBorderPickups.cross_border.page_objects.UI.LoginPage.login_page import LoginPage

# @pytest.fixture(params=[BaseConstants.CHROME_BROWSER])
# def init_driver(request: 'SubRequest'):
#     """ Initialize given driver and open application URL """
#     web_driver = None
# 
#     if request.param == "Chrome":
#         if platform.system() == BaseConstants.WINDOWS_SYSTEM:
#             web_driver = webdriver.Chrome(executable_path=config.Config.WINDOWS_CHROME_DRIVER_DIR)
#         else:
#             chrome_options = Options()
#             chrome_options.add_argument("--headless")
#             chrome_options.add_argument('--no-sandbox')
#             chrome_options.add_argument("--window-size=1920,1080")
#             chrome_options.add_argument("--disable-extensions")
#             chrome_options.add_argument("--start-maximized")
#             chrome_options.add_argument('--ignore-certificate-errors')
#             chrome_options.add_argument('--allow-running-insecure-content')
# 
#             web_driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver', options=chrome_options)
#     elif request.param == "firefox":
#         web_driver = webdriver.Firefox(executable_path=config.Config.FIREFOX_DRIVER_DIR)
# 
#     request.cls.driver = web_driver
#     web_driver.get(url=BaseConstants.DEFAULT_BASE_URL)
#     web_driver.implicitly_wait(time_to_wait=BaseConstants.DEFAULT_TIMEOUT)
# 
#     yield web_driver
# 
#     web_driver.quit()
# 
# 
# @pytest.fixture()
# def login(init_driver):
#     """ Automatically logs into product with configured username and password before each test """
#     driver = init_driver
# 
#     try:
#         login_page = LoginPage(driver)
#         login_page.do_login()
#         driver.implicitly_wait(time_to_wait=BaseConstants.DEFAULT_TIMEOUT)
#     except Exception as e:
#         raise Exception("Throws exception while login, Exception :: {}".format(e))


@pytest.fixture(params=[CBP.CBP_TEST_ENVIRONMENT])
def init_driver(request: 'SubRequest'):
    """ Initialize given driver and open application URL """
    global web_driver
    capabilities = config.Config.CAPABILITIES

    try:
        if request.param == BaseConstants.LOCAL:
            if capabilities["browserName"].casefold() == BaseConstants.CHROME_BROWSER.casefold():
                if config.Config.PLATFORM_NAME == BaseConstants.WINDOWS_SYSTEM:
                    web_driver = webdriver.Chrome(executable_path=config.Config.WINDOWS_CHROME_DRIVER_DIR)
                else:
                    os.chmod(path=config.Config.LINUX_CHROME_DRIVER_DIR, mode=755)
                    chrome_options = Options()
                    chrome_options.binary_location = BaseConstants.CHROME_BINARY_LOCATION
                    web_driver = webdriver.Chrome(chrome_options=chrome_options,
                                                  executable_path=config.Config.LINUX_CHROME_DRIVER_DIR)
            elif capabilities["browserName"] == BaseConstants.FIREFOX_BROWSER:
                web_driver = webdriver.Firefox(executable_path=config.Config.FIREFOX_DRIVER_DIR)
        else:
            web_driver = webdriver.Remote(command_executor=BaseConstants.Urls.GRID_HUB_URL,
                                          desired_capabilities=capabilities)

        request.cls.driver = web_driver
        web_driver.maximize_window()
        web_driver.get(url=CBP.APPLICATION_URL)
        web_driver.implicitly_wait(time_to_wait=BaseConstants.DEFAULT_TIMEOUT)

        yield web_driver
    finally:
        web_driver.quit()


def get_driver_instance():
    """ Returns driver instance """
    return web_driver


@pytest.fixture()
def login(init_driver):
    """ Automatically logs into product with configured username and password before each test """
    driver = init_driver

    try:
        login_page = LoginPage(driver)
        login_page.do_login()

        expected_locator = Locators.HeaderPage.operation_button if "-ops-" in driver.current_url else \
            Locators.HeaderPage.user_avatar
        login_page.wait_for_element(lambda: WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
            expected_locator)), waiting_for="dashboard gets displayed after login")
        yield
    finally:
        HeaderPage(driver).do_logout()


def _test_status(call: 'CallInfo', test_report: 'TestReport') -> BaseConstants.Status:
    """ Return test status from test report """
    if call.excinfo and test_report.outcome == 'failed':
        if call.when == "call" and isinstance(call.excinfo.value, AssertionError):
            return BaseConstants.Status.Failed
        return BaseConstants.Status.Error

    if hasattr(test_report, 'wasxfail'):
        if test_report.skipped:
            return BaseConstants.Status.XFailed
        elif test_report.passed:
            return BaseConstants.Status.XPassed
        raise AttributeError('wasxfail present but treport.skipped and report.passed are False!')

    if test_report.skipped:
        return BaseConstants.Status.Skipped

    return BaseConstants.Status.Passed


def get_screenshot_filename(test_name: str, test_status: BaseConstants.Status = None) -> str:
    """
    Return test's screenshot filename

    :param str test_name: test case name
    :param str test_status: test case status
    :return: screenshot filename
    :rtype: str
    """
    filename_prefix = '{}-'.format(test_status.value) if test_status != BaseConstants.Status.Passed else ''
    screenshot_filename = ".".join([os.path.split(test_name)[1], BaseConstants.SCREENSHOT_EXTENSION])

    return "{}{}".format(filename_prefix, screenshot_filename)


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """ Pytest hook that generates screenshots for failed tests """
    outcome = yield

    driver = web_driver
    pytest_html = item.config.pluginmanager.getplugin('html')

    report = outcome.get_result()
    test_status = _test_status(call, report)

    if call.when in ('setup', 'call'):
        item.cls.has_failed = test_status in (BaseConstants.Status.Failed, BaseConstants.Status.Error)

    if not report.passed:
        report.exception = getattr(call.excinfo.type, '__name__', " ")
        report.exception_text = getattr(call.excinfo.value, 'msg', " ")

        path, class_name, test_name = item.nodeid.split("::")
        file_name = get_screenshot_filename(test_name=test_name, test_status=test_status)

        # BasePage(driver).take_screenshot(filename=file_name)
        extra = getattr(report, 'extra', [])

        for screenshot in getattr(report, 'CBP_screenshots', []):
            with open(screenshot, "rb") as image_file:
                encoded_string = base64.b64encode(image_file.read())
                base64_image = encoded_string.decode()
                extra.append(pytest_html.extras.png(base64_image))

        report.extra = extra

