import random

import pytest
from _pytest.fixtures import SubRequest

from CrossBorderPickups.cross_border.lib.constants.constant import PageConstants, BaseConstants
from CrossBorderPickups.cross_border.lib.helpers.helpers import generate_random_tracking_number
from CrossBorderPickups.cross_border.lib.locators.locators import Locators
from CrossBorderPickups.cross_border.page_objects.UI.Operations.NewPackagesPage.new_packages_page import NewPackagesPage
from CrossBorderPickups.cross_border.tests.conftest import get_driver_instance


@pytest.fixture()
def create_new_package(request: 'SubRequest', login):
    """ This fixture created new package from operation portal """

    driver = get_driver_instance()
    new_package_page = NewPackagesPage(driver)
    new_package_page.open(url=BaseConstants.Urls.NEW_PACKAGES_PAGE_URL)

    new_package_constant = PageConstants.NewPackagePage
    carrier = random.sample(new_package_constant.PackageCarrier.CARRIERS, k=1)[0]
    tracking_number = generate_random_tracking_number()
    vendor = random.sample(new_package_constant.PackageVendors.VENDORS, k=1)[0]
    weight = random.randint(1, 9)

    full_name = request.param.get("full_name") if hasattr(request, 'param') else "QA Automation"
    package_status = request.param.get("package_status") if hasattr(request, 'param') else \
        new_package_constant.PackageStatus.PENDING_ORDER_CREATION
    package_carrier = request.param.get("incoming_carrier") if hasattr(request, 'param') else carrier
    tracking_number = request.param.get("tracking_number") if hasattr(request, 'param') else tracking_number
    package_vendor = request.param.get("package_vendor") if hasattr(request, 'param') else vendor
    package_weight = request.param.get("package_weight") if hasattr(request, 'param') else weight

    package_details_dict = {"full_name": full_name, "status": package_status, "incoming_carrier": package_carrier,
                            "tracking_number": tracking_number, "vendor": package_vendor, "weight": package_weight}

    new_package_page.fill_package_information(**package_details_dict)
    new_package_page.click(by_locator=Locators.NewPackagesPage.create_package_button)

    yield package_details_dict
