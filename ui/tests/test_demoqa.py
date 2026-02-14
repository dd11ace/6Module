import time
from playwright.sync_api import Page, expect
from constants import DEMOQA_TEXT_BOX_LINK, DEMOQA_WEBTABLES_LINK


def test_text_box(page: Page):
    page.goto(DEMOQA_TEXT_BOX_LINK)

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


def test_add_button_and_registration(page: Page):
    page.goto(DEMOQA_WEBTABLES_LINK)

    page.get_by_role("button", name="Add").click()
    page.get_by_text("Registration Form").is_visible()
    page.get_by_role("textbox", name="First Name").fill("John")
    page.get_by_role("textbox", name="Last Name").fill("Doe")
    page.get_by_role("textbox", name="name@example.com").fill("example@example.com")
    page.get_by_role("textbox", name="Age").fill("30")
    page.get_by_role("textbox", name="Salary").fill("300000")
    page.get_by_role("textbox", name="Department").fill("QA")

    page.get_by_role("button", name="Submit").click()

    expect(
        page.get_by_role(
            "row", name="First Name Last Name Age Email Salary Department Action"
        )
    ).to_be_visible()
    expect(
        page.get_by_role("row", name="John Doe 30 example@example.com 300000 QA")
    ).to_be_visible()

    time.sleep(10)
