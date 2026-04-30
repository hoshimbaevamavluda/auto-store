import allure
import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture
def page():
    with sync_playwright() as drv:
        browser = drv.chromium.launch(headless=False, slow_mo=5000)
        page = browser.new_page()
        page.set_default_timeout(5000)
        yield page
        browser.close()


@pytest.hookimpl( tryfirst=True, wrapper=True)
def pytest_runtest_makereport(item, call):
    rep=yield
    node = rep.nodeid.replace("::", "_").replace(".", "_")
    file_path = f"screenshot_{node}.png"
    if rep.when == "call" and rep.failed:
        page_ = item.funcargs.get("page")
        page_.screenshot(path=file_path)

        with open(file_path, "rb") as f:
            allure.attach(
                f.read(),
                name=f"Кадр при подении {item.name}",
                attachment_type=allure.attachment_type.PNG,
            )
    return rep