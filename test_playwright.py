import time
from playwright.sync_api import Page


def test_example(page: Page):
    page.goto("https://www.example.com")
    time.sleep(10)


def test_google(page: Page):
    page.goto("https://www.google.com")
    time.sleep(10)
