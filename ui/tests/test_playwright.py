import time
from playwright.sync_api import Page

from constants import EXAMPLE_LINK, GOOGLE_LINK


def test_example(page: Page):
    page.goto(EXAMPLE_LINK)
    time.sleep(10)


def test_google(page: Page):
    page.goto(GOOGLE_LINK)
    time.sleep(10)
