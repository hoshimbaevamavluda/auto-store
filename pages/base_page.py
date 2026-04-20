from playwright.sync_api import expect

from config.base import BASE_URL


class BasePage:
    def __init__(self, page):
        self.page = page

    def expect_to_have_url(self, url_sub: str):
        expect(self.page).to_have_url(BASE_URL)

    def click(
        self,
        locator,
        button: str = "left",
        click_count: int = 1,
        no_wait_after: bool = False,
    ) -> None:
        if isinstance(locator, str):
            locator = self.page.locator(locator)
        locator.click(
            button=button, click_count=click_count, no_wait_after=no_wait_after
        )