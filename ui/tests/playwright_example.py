import time
from playwright.sync_api import sync_playwright

from constants import DEMOQA_MAIN_LINK

playwright = sync_playwright().start()

browser = playwright.chromium.launch(headless=False)
page = browser.new_page()
page.goto(DEMOQA_MAIN_LINK)
time.sleep(10)

browser.close()

playwright.stop()
