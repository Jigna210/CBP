import os
import platform

import pytest
from _pytest.fixtures import SubRequest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from CrossBorderPickups.cross_border.lib.configs import config
from CrossBorderPickups.cross_border.lib.constants.constant import BaseConstants
from CrossBorderPickups.cross_border.page_objects.UI.LoginPage.login_page import LoginPage


@pytest.fixture(params=[CBP.CBP_TEST_ENVIRONMENT])
def init_driver(request: 'SubRequest'):
    """ Initialize given driver and open application URL """
    web_driver = None
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

# @pytest.fixture(params=[BaseConstants.BROWSER])
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


@pytest.fixture()
def login(init_driver):
    """ Automatically logs into product with configured username and password before each test """
    driver = init_driver

    try:
        login_page = LoginPage(driver)
        login_page.do_login()

        login_page.wait_for_element(lambda: WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.HeaderPage.operation_button)),
                                    waiting_for="dashboard gets displayed after login")
    except Exception as e:
        raise "Throws exception while login, Exception :: {}".format(e)

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
