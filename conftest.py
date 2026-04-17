import pytest
from playwright.sync_api import sync_playwright

from config.base import BASE_URL


@pytest.fixture(autouse=True)
def page():
    with sync_playwright() as drv:
        browser = drv.chromium.launch(headless=True, slow_mo=5000)
        page = browser.new_page()
        page.set_default_timeout(3000)
        page.goto(BASE_URL)
        yield page
        browser.close()