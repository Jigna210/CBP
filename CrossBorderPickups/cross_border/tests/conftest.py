import os
import platform

import pytest
from _pytest.fixtures import SubRequest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from CrossBorderPickups.cross_border.lib.configs import config
from CrossBorderPickups.cross_border.lib.constants.constant import BaseConstants
from CrossBorderPickups.cross_border.page_objects.UI.LoginPage.login_page import LoginPage


@pytest.fixture(params=[BaseConstants.CHROME_BROWSER])
def init_driver(request: 'SubRequest'):
    """ Initialize given driver and open application URL """
    web_driver = None

    if request.param == "Chrome":
        if platform.system() == BaseConstants.WINDOWS_SYSTEM:
            web_driver = webdriver.Chrome(executable_path=config.Config.WINDOWS_CHROME_DRIVER_DIR)
        else:
            chrome_options = Options()
            chrome_options.add_argument("--headless")
            chrome_options.add_argument('--no-sandbox')
            chrome_options.add_argument("--window-size=1920,1080")
            chrome_options.add_argument("--disable-extensions")
            chrome_options.add_argument("--start-maximized")
            chrome_options.add_argument('--ignore-certificate-errors')
            chrome_options.add_argument('--allow-running-insecure-content')

            web_driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver', options=chrome_options)
    elif request.param == "firefox":
        web_driver = webdriver.Firefox(executable_path=config.Config.FIREFOX_DRIVER_DIR)

    request.cls.driver = web_driver
    web_driver.get(url=BaseConstants.DEFAULT_BASE_URL)
    web_driver.implicitly_wait(time_to_wait=BaseConstants.DEFAULT_TIMEOUT)

    yield web_driver

    web_driver.quit()
    

@pytest.fixture()
def login(init_driver):
    """ Automatically logs into product with configured username and password before each test """
    driver = init_driver

    try:
        login_page = LoginPage(driver)
        login_page.do_login()
        driver.implicitly_wait(time_to_wait=BaseConstants.DEFAULT_TIMEOUT)
    except Exception as e:
        raise Exception("Throws exception while login, Exception :: {}".format(e))
