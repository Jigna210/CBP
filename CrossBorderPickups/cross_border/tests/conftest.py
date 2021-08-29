import pytest
from selenium import webdriver

from CrossBorderPickups.cross_border.lib.configs import config
from CrossBorderPickups.cross_border.lib.constants.constant import BaseConstants
from CrossBorderPickups.cross_border.page_objects.UI.LoginPage.login_page import LoginPage


@pytest.fixture(params=["chrome"], scope="class")
def init_driver(request):
    """ Initialize given driver and open application URL """
    web_driver = None

    if request.param == "chrome":
        web_driver = webdriver.Chrome(executable_path=config.Config.CHROME_DRIVER_DIR)
    elif request.param == "firefox":
        web_driver = webdriver.Firefox(executable_path=config.Config.FIREFOX_DRIVER_DIR)

    request.cls.driver = web_driver
    web_driver.get(url=BaseConstants.Urls.BASE_URL)
    web_driver.implicitly_wait(time_to_wait=BaseConstants.DEFAULT_TIMEOUT)

    yield

    web_driver.close()


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
