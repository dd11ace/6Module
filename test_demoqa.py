import time
from playwright.sync_api import Page, expect


def test_text_box(page: Page):
    page.goto("https://demoqa.com/text-box")

    # вариант 1
    # username_locator = "#userName"
    # page.fill(username_locator, "testQa")

    # Вариант 2
    # page.locator("#userName").fill("testQa")

    # Вариант 3
    # page.fill(selector="#userName", value="testQa")

    # Вариант 4
    page.get_by_role("textbox", name="Full Name").fill("testQa")
    page.get_by_role("textbox", name="name@example.com").fill("test@qa.com")
    page.get_by_role("textbox", name="Current Address").fill("Phuket, Thalang 99")
    page.fill("#permanentAddress", "Moscow, Mashkova 1")

    page.get_by_role("button", name="Submit").click()

    expect(page.locator("#output")).to_be_visible()
    expect(page.locator("#output #name")).to_have_text("Name:testQa")
    expect(page.locator("#output #email")).to_have_text("Email:test@qa.com")
    expect(page.locator("#output #currentAddress")).to_have_text(
        "Current Address :Phuket, Thalang 99"
    )
    expect(page.locator("#output #permanentAddress")).to_have_text(
        "Permananet Address :Moscow, Mashkova 1"
    )

    time.sleep(10)
