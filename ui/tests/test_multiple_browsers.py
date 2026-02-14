import time
from playwright.sync_api import sync_playwright

from constants import EXAMPLE_LINK, GOOGLE_LINK


def test_multiple_browsers():
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
