import pytest
from faker import Faker
from playwright.sync_api import sync_playwright


# @pytest.fixture
# def page():
#     with sync_playwright() as drv:
#         browser = drv.chromium.launch(headless=False, slow_mo=5000)
#         page = browser.new_page()
#         page.set_default_timeout(5000)
#         yield page
#         browser.close()

@pytest.fixture(scope="function")
def mobile(request):
    with sync_playwright() as p:
        device_name = getattr(request, "param", "iPhone 11")
        device = p.devices[device_name]

        browser_type = p.webkit if "iPhone" in device_name or "iPad" in device_name else p.chromium
        browser = browser_type.launch(headless=False, slow_mo=500)

        context = browser.new_context(**device)
        page = context.new_page()

        yield page

        context.close()
        browser.close()



@pytest.fixture
def page(request):
    browser_ = "_X_"
    if hasattr(request, "param"):
        browser_ = "chrome"
        if isinstance(request.param, tuple):
            headless_ = request.param[0]
            if len(request.param) > 1:
                browser_ = request.param[1]
        else:
            headless_ = request.param
    else:
        headless_ = False
    with (sync_playwright() as drv):
        bro_name = request.config.getoption("--bro")
        if browser_ == "chrome":
            drv_bro = drv.chromium
        elif browser_ == "firefox":
            drv_bro = drv.firefox
        elif browser_ == "safari" or browser_ == "webkit":
            drv_bro = drv.webkit
        else:
            if bro_name == "chrome" or bro_name == "chromium":
                drv_bro = drv.chromium
            elif bro_name == "firefox":
                drv_bro = drv.firefox
            elif bro_name == "safari":
                drv_bro = drv.webkit
            else:
                drv_bro = drv.chromium

        print(f"{browser_=} {bro_name=}")
        browser = drv_bro.launch(headless=headless_, slow_mo=500)
        page = browser.new_page()
        page.set_default_timeout(4_000)  # 1_100
        yield page
        browser.close()
