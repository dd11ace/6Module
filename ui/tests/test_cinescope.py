import pytest
import allure
import time
from random import randint
from playwright.sync_api import Page, expect

from constants import CINESCOPE_LOGIN_LINK, CINESCOPE_REGISTER_LINK


@allure.epic("Позитивные UI сценарии для Cinescope")
@allure.label("qa_name", "Ivan Petrovich")
@allure.tag("ui", "positive")
@allure.title("Позитивные UI Тесты для Cinescope")
@pytest.mark.ui
@pytest.mark.positive
class TestCinescope:
    """Позитивные UI тесты для Cinescope"""

    @allure.feature("Тест функциональности text box")
    @allure.story("Пользователь может заполнить тестовое поле")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("Провека функциональности text box")
    @allure.tag("smoke", "input-validation")
    @pytest.mark.critical
    @pytest.mark.smoke
    @pytest.mark.regression
    def test_text_box(self, page: Page):
        """Тестирование поля ввода text box"""
        page.goto(CINESCOPE_REGISTER_LINK)

        with allure.step("Заполнение поля"):
            page.get_by_role("textbox", name="Имя Фамилия Отчество").fill(
                "Жмышенко Валерий Альбертович"
            )

        time.sleep(10)

    @allure.feature("Регистрация")
    @allure.story("Пользователь может зарегестрироваться")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("Проверка заполнения и отправки формы регистрации")
    @pytest.mark.critical
    @pytest.mark.smoke
    @pytest.mark.regression
    def test_registration(self, page: Page):
        """Тестирование регистрации пользователя"""
        page.goto(CINESCOPE_REGISTER_LINK)

        user_email = f"test_{randint(1, 9999)}@email.qa"
        with allure.step("Заполнение полей формы"):
            page.get_by_role("textbox", name="Имя Фамилия Отчество").fill(
                "Жмышенко Валерий Альбертович"
            )
            page.get_by_role("textbox", name="Email").fill(user_email)
            page.get_by_role("textbox", name="Пароль", exact=True).fill("qwerty123Q")
            page.get_by_role("textbox", name="Повторите пароль").fill("qwerty123Q")
        with allure.step("Отправка формы"):
            page.get_by_role("button", name="Зарегистрироваться").click()
        with allure.step("Проверка успешной отправки"):
            page.wait_for_url(CINESCOPE_LOGIN_LINK)
            expect(page.get_by_text("Подтвердите свою почту")).to_be_visible()

        time.sleep(10)
