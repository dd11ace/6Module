import time
from random import randint
from playwright.sync_api import Page, expect

from constants import CINESCOPE_LOGIN_LINK, CINESCOPE_REGISTER_LINK


def test_text_box(page: Page):
    page.goto(CINESCOPE_REGISTER_LINK)

    page.get_by_role("textbox", name="Имя Фамилия Отчество").fill(
        "Жмышенко Валерий Альбертович"
    )

    time.sleep(10)


def test_registration(page: Page):
    page.goto(CINESCOPE_REGISTER_LINK)

    user_email = f"test_{randint(1, 9999)}@email.qa"

    page.get_by_role("textbox", name="Имя Фамилия Отчество").fill(
        "Жмышенко Валерий Альбертович"
    )
    page.get_by_role("textbox", name="Email").fill(user_email)
    page.get_by_role("textbox", name="Пароль", exact=True).fill("qwerty123Q")
    page.get_by_role("textbox", name="Повторите пароль").fill("qwerty123Q")

    page.get_by_role("button", name="Зарегистрироваться").click()

    page.wait_for_url(CINESCOPE_LOGIN_LINK)
    expect(page.get_by_text("Подтвердите свою почту")).to_be_visible()

    time.sleep(10)
