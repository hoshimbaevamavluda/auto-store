import expect

from pages.home_page import HomePage


class TestCheck:

    def test_ats_001(self, page):
        hm_page = HomePage(page)
        hm_page.open_page()
        expect(page).to_have_url("/", timeout=10000)