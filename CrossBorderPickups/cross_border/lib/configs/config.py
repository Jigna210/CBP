import os
import platform

from selenium.webdriver import DesiredCapabilities

from CrossBorderPickups.cross_border.lib.configs.environmental_variables import CBP
from CrossBorderPickups.cross_border.lib.constants.constant import BaseConstants


class Config(object):
    """ Configuration variables related to automation framework """

    PROJECT_ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    WINDOWS_CHROME_DRIVER_DIR = os.path.join(PROJECT_ROOT_DIR,
                                             os.path.join("drivers", "chrome_driver", "chromedriver.exe"))
    LINUX_CHROME_DRIVER_DIR = os.path.join(PROJECT_ROOT_DIR, os.path.join("drivers", "chrome_driver", "chromedriver"))
    FIREFOX_DRIVER_DIR = os.path.join(PROJECT_ROOT_DIR, os.path.join("drivers", "firefox_driver", "geckodriver.exe"))
    PLATFORM_NAME = platform.system()
    SCREENSHOTS_DIR = os.path.join(PROJECT_ROOT_DIR, os.path.join("output", "screenshots"))
    CAPABILITIES = DesiredCapabilities.CHROME if CBP.CBP_TEST_BROWSER == BaseConstants.CHROME_BROWSER else \
        DesiredCapabilities.FIREFOX
