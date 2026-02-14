import time
from datetime import datetime
from playwright.sync_api import Page, expect
from constants import (
    DEMOQA_CHECKBOX_LINK,
    DEMOQA_DYNAMIC_PROPERTIES_LINK,
    DEMOQA_RADIO_BUTTONS_LINK,
    DEMOQA_REGISTRATION_FORM_LINK,
    DEMOQA_TEXT_BOX_LINK,
    DEMOQA_WEBTABLES_LINK,
)


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


def test_registration_form(page: Page):
    page.goto(DEMOQA_REGISTRATION_FORM_LINK)

    today = datetime.now().strftime("%d %b %Y")

    page.get_by_role("textbox", name="First Name").fill("John")
    page.get_by_role("textbox", name="Last Name").fill("Doe")
    page.get_by_role("textbox", name="name@example.com").fill("example@example.com")

    page.get_by_role("radio", name="Male", exact=True).check(force=True)
    page.locator('[for="gender-radio-1"]').click()

    page.get_by_role("textbox", name="Mobile Number").fill("1234567890")

    expect(page.locator("#dateOfBirthInput")).to_have_value(today)
    date_of_birth = page.get_attribute("#dateOfBirthInput")
    print(date_of_birth)

    page.locator("#subjectsInput").fill("English")
    expect(page.locator(".subjects-auto-complete__menu")).to_be_visible()
    page.locator("#react-select-2-option-0").click()

    page.locator('[for="hobbies-checkbox-1"]').click()
    page.locator('[for="hobbies-checkbox-2"]').click()
    page.locator('[for="hobbies-checkbox-3"]').click()

    page.get_by_role("textbox", name="Current Address").fill("Moscow, Mashkova 1")

    page.locator("#state").click()
    page.locator("#react-select-3-option-0").click()
    page.locator("#city").click()
    page.locator("#react-select-4-option-0").click()

    expect(
        page.get_by_text("© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.")
    ).to_be_visible()

    page.get_by_role("button", name="Submit").click()

    expect(page.get_by_text("Thanks for submitting the form")).to_be_visible()

    time.sleep(5)


def test_radio_buttons(page: Page):
    page.goto(DEMOQA_RADIO_BUTTONS_LINK)

    page.is_enabled("#yesRadio")
    page.is_enabled("#impressiveRadio")
    page.is_disabled("#noRadio")

    time.sleep(3)


def test_checkbox(page: Page):
    page.goto(DEMOQA_CHECKBOX_LINK)

    page.get_by_role("treeitem", name="Select Home Home").is_visible()
    page.get_by_role("treeitem", name="Select Desktop Desktop").is_hidden()

    page.locator(".rc-tree-switcher").click()
    page.get_by_role("treeitem", name="Select Desktop Desktop").is_visible()

    time.sleep(3)


def test_dynamic_properties(page: Page):

    page.goto(DEMOQA_DYNAMIC_PROPERTIES_LINK)

    expect(
        page.get_by_role("button", name="Visible After 5 Seconds")
    ).not_to_be_visible()
    page.get_by_role("button", name="Will enable 5 Seconds").is_disabled()
    page.wait_for_selector("#visibleAfter")
    page.get_by_role("button", name="Visible After 5 Seconds").is_visible()
    page.get_by_role("button", name="Will enable 5 Seconds").is_enabled()

    time.sleep(3)


def test_expect(page: Page):
    page.goto(DEMOQA_RADIO_BUTTONS_LINK)

    yes_radio = page.get_by_role("radio", name="Yes")
    impressive_radio = page.get_by_role("radio", name="Impressive")
    no_radio = page.get_by_role("radio", name="No")
    expect(no_radio).to_be_disabled()
    expect(yes_radio).to_be_enabled()
    expect(impressive_radio).to_be_enabled()
    page.locator('[for="yesRadio"]').click()
    expect(yes_radio).to_be_checked()
    expect(impressive_radio).not_to_be_checked()

    time.sleep(3)
