import time
from playwright.sync_api import Page, sync_playwright

from constants import EXAMPLE_LINK, GOOGLE_LINK, WIKIPEDIA_LINK, YANDEX_LINK


class TestPlaywright:
    def test_example(self, page: Page):
        page.goto(EXAMPLE_LINK)
        time.sleep(10)

    def test_google(self, page: Page):
        page.goto(GOOGLE_LINK)
        time.sleep(10)

    def test_some_entities(self):
        with sync_playwright() as p:
            browser1 = p.chromium.launch(headless=False)

            context1_1 = browser1.new_context()
            context1_2 = browser1.new_context()

            page1_1_1 = context1_1.new_page()
            page1_1_2 = context1_1.new_page()
            page1_2_1 = context1_2.new_page()
            page1_2_2 = context1_2.new_page()

            page1_1_1.goto(EXAMPLE_LINK)
            page1_1_2.goto(GOOGLE_LINK)
            page1_2_1.goto(WIKIPEDIA_LINK)
            page1_2_2.goto(YANDEX_LINK)

            time.sleep(10)

            page1_1_1.close()
            page1_1_2.close()
            page1_2_1.close()
            page1_2_2.close()

            context1_1.close()
            context1_2.close()

            browser1.close()

    def test_multiple_browsers(self):
        with sync_playwright() as p:
            chromium_browser = p.chromium.launch(headless=False)
            firefox_browser = p.firefox.launch(headless=False)

            chromium_page = chromium_browser.new_page()
            firefox_page = firefox_browser.new_page()

            chromium_page.goto(EXAMPLE_LINK)
            firefox_page.goto(GOOGLE_LINK)

            time.sleep(10)

            chromium_browser.close()
            firefox_browser.close()
