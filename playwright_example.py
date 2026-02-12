import time
from playwright.sync_api import sync_playwright

playwright = sync_playwright().start()

browser = playwright.chromium.launch(headless=False)
page = browser.new_page("https://demoqa.com/")
time.sleep(10)

browser.close()

playwright.stop()
