import random

import pytest
from _pytest.fixtures import SubRequest

from CrossBorderPickups.cross_border.lib.constants.constant import PageConstants, BaseConstants
from CrossBorderPickups.cross_border.lib.helpers.helpers import generate_random_tracking_number, sleep_execution
from CrossBorderPickups.cross_border.lib.locators.locators import Locators
from CrossBorderPickups.cross_border.lib.utility.notification import Notifications
from CrossBorderPickups.cross_border.page_objects.UI.LoginPage.login_page import LoginPage
from CrossBorderPickups.cross_border.page_objects.UI.Operations.NewPackagesPage.new_packages_page import NewPackagesPage
from CrossBorderPickups.cross_border.tests.conftest import get_driver_instance

app_url = BaseConstants.OPERATION_PORTAL_URL
app_user_name = BaseConstants.OPERATION_PORTAL_USERNAME
app_password = BaseConstants.OPERATION_PORTAL_PASSWORD


@pytest.fixture()
def create_new_package(request: 'SubRequest', login):
    """ This fixture created new package from operation portal """

    created_pkg_details = []
    pkg_count = request.param.get('pkg_count') if hasattr(request, 'param') and 'pkg_count' in request.param else 1

    driver = get_driver_instance()
    LoginPage(driver).login_in_portal_with_credentials(driver_instance=driver, portal_url=app_url,
                                                       user_name=app_user_name, password=app_password)

    new_package_page = NewPackagesPage(driver)
    new_package_page.open(url=BaseConstants.Urls.NEW_PACKAGES_PAGE_URL)
    new_package_constant = PageConstants.NewPackagePage

    for _ in range(pkg_count):
        package_details_dict = {}
        carrier = random.sample(new_package_constant.PackageCarrier.CARRIERS, k=1)[0]
        tracking_number = generate_random_tracking_number()
        vendor = random.sample(new_package_constant.PackageVendors.VENDORS, k=1)[0]
        weight = random.randint(1, 9)

        package_data_dict = {"full_name": "QA Automation", "status": new_package_constant.PackageStatus.PENDING_PAYMENT,
                             "incoming_carrier": carrier, "tracking_number": tracking_number, "vendor": vendor,
                             "weight": weight}

        for field in ["full_name", "status", "incoming_carrier", "tracking_number", "vendor", "weight"]:
            if field in list(request.param.keys()):
                package_details_dict[field] = request.param.get(field)
            else:
                package_details_dict[field] = package_data_dict.get(field)

        new_package_page.fill_package_information(**package_details_dict)
        sleep_execution(2)

        new_package_locator = Locators.NewPackagesPage
        new_package_page.click(by_locator=new_package_locator.add_content_button)
        sleep_execution(2)

        new_package_page.click(by_locator=Locators.ops_modal_title)
        content_category = random.sample(new_package_constant.AddContent.CONTENT_CATEGORY, k=1)[0]

        package_content_dict = {"category": content_category, "quantity": random.randint(1, 9),
                                "value": random.randint(1, 9)}

        new_package_page.fill_content_information(**package_content_dict)
        new_package_page.click(by_locator=new_package_locator.AddContent.add_button)

        sleep_execution(2)
        new_package_page.click(by_locator=new_package_locator.create_update_package_button)

        new_package_page.wait_for_element(lambda: Notifications(driver).is_element_visible(
            by_locator=Locators.Notification.ops_notification_msg_text))
        created_pkg_details.append(package_details_dict)

    yield created_pkg_details
