import pytest
from faker import Faker
from playwright.sync_api import sync_playwright


@pytest.fixture
def page():
    with sync_playwright() as drv:
        browser = drv.chromium.launch(headless=False, slow_mo=5000)
        page = browser.new_page()
        page.set_default_timeout(5000)
        yield page
        browser.close()


@pytest.fixture
def fake_data():
    return Faker()
