import os
import platform

import pytest
from _pytest.fixtures import SubRequest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from CrossBorderPickups.cross_border.lib.configs import config
from CrossBorderPickups.cross_border.lib.constants.constant import BaseConstants
from CrossBorderPickups.cross_border.page_objects.UI.LoginPage.login_page import LoginPage


@pytest.fixture(params=[BaseConstants.BROWSER])
def init_driver(request: 'SubRequest'):
    """ Initialize given driver and open application URL """
    web_driver = None

    if request.param == "chrome":
        if platform.system() == BaseConstants.WINDOWS_SYSTEM:
            web_driver = webdriver.Chrome(executable_path=config.Config.WINDOWS_CHROME_DRIVER_DIR)
        else:
            #print(config.Config.LINUX_CHROME_DRIVER_DIR)
            #os.chmod(path=config.Config.LINUX_CHROME_DRIVER_DIR, mode=755)
            chrome_options = Options()
            chrome_options.add_argument("--headless")
            chrome_options.add_argument('--no-sandbox')
            web_driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver', options=chrome_options)
    elif request.param == "firefox":
        web_driver = webdriver.Firefox(executable_path=config.Config.FIREFOX_DRIVER_DIR)

    request.cls.driver = web_driver
    web_driver.maximize_window()
    web_driver.get(url=BaseConstants.Urls.BASE_URL)
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
