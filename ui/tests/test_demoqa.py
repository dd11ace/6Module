import pytest
import allure
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


@allure.epic("Demoqa UI Тесты")
@allure.label("qa_name", "Ivan Petrovich")
@allure.tag("ui", "positive")
@allure.title("Позитивные Demoqa UI Тесты")
@pytest.mark.ui
@pytest.mark.positive
class TestDemoqa:
    """Класс для позитивных UI тестов для Demoqa"""

    @allure.feature("Тест функциональности text box")
    @allure.story("Пользователь отправляет данные через форму")
    @allure.title("Проверка отправки формы с валидными данными")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.normal
    @pytest.mark.regression
    @pytest.mark.smoke
    def test_text_box(self, page: Page):
        """Позитивные UI тесты для Demoqa"""
        page.goto(DEMOQA_TEXT_BOX_LINK)

        with allure.step("Заполнение полей"):
            page.get_by_role("textbox", name="Full Name").fill("testQa")
            page.get_by_role("textbox", name="name@example.com").fill("test@qa.com")
            page.get_by_role("textbox", name="Current Address").fill(
                "Phuket, Thalang 99"
            )
            page.fill("#permanentAddress", "Moscow, Mashkova 1")
        with allure.step("Отправка формы"):
            page.get_by_role("button", name="Submit").click()
        with allure.step("Валидация результатов"):
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

    @allure.feature("Функциональность веб таблицы")
    @allure.story("Пользователь может добавить новую запись")
    @allure.title('Проверка кнопки "add" и заполнение')
    @allure.description(
        'Проверка кнопки "add", заполнение формы и добавление данных в таблицу'
    )
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.critical
    @pytest.mark.smoke
    @pytest.mark.regression
    def test_web_table(self, page: Page):
        page.goto(DEMOQA_WEBTABLES_LINK)

        with allure.step("Открытие формы"):
            page.get_by_role("button", name="Add").click()
        with allure.step("Заполнение формы"):
            page.get_by_text("Registration Form").is_visible()
            page.get_by_role("textbox", name="First Name").fill("John")
            page.get_by_role("textbox", name="Last Name").fill("Doe")
            page.get_by_role("textbox", name="name@example.com").fill(
                "example@example.com"
            )
            page.get_by_role("textbox", name="Age").fill("30")
            page.get_by_role("textbox", name="Salary").fill("300000")
            page.get_by_role("textbox", name="Department").fill("QA")
        with allure.step("Отправка формы"):
            page.get_by_role("button", name="Submit").click()
        with allure.step("Валидация данных таблицы"):
            expect(
                page.get_by_role(
                    "row",
                    name="First Name Last Name Age Email Salary Department Action",
                )
            ).to_be_visible()
            expect(
                page.get_by_role(
                    "row", name="John Doe 30 example@example.com 300000 QA"
                )
            ).to_be_visible()

        time.sleep(10)

    @allure.feature("Регистрация")
    @allure.story("Пользователь может зарегестрироваться")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("Проверка заполнения и отправки формы регистрации")
    @pytest.mark.critical
    @pytest.mark.smoke
    @pytest.mark.regression
    def test_registration_form(self, page: Page):
        page.goto(DEMOQA_REGISTRATION_FORM_LINK)

        today = datetime.now().strftime("%d %b %Y")
        with allure.step("Заполенение данных"):
            page.get_by_role("textbox", name="First Name").fill("John")
            page.get_by_role("textbox", name="Last Name").fill("Doe")
            page.get_by_role("textbox", name="name@example.com").fill(
                "example@example.com"
            )

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

            page.get_by_role("textbox", name="Current Address").fill(
                "Moscow, Mashkova 1"
            )

            page.locator("#state").click()
            page.locator("#react-select-3-option-0").click()
            page.locator("#city").click()
            page.locator("#react-select-4-option-0").click()
        with allure.step("Проверка надписи в footer"):
            expect(
                page.get_by_text("© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.")
            ).to_be_visible()
        with allure.step("Отправка формы"):
            page.get_by_role("button", name="Submit").click()
        with allure.step("Проверка успешной отправки"):
            expect(page.get_by_text("Thanks for submitting the form")).to_be_visible()

        time.sleep(5)

    @allure.feature("Функциональность радио кнопок")
    @allure.story("Состояния радио кнопок")
    @allure.title("Проверка функциональности радио кнопок в разных состояниях")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.normal
    def test_radio_buttons(self, page: Page):
        page.goto(DEMOQA_RADIO_BUTTONS_LINK)

        with allure.step("Валидация состояний радио кнопок"):
            page.is_enabled("#yesRadio")
            page.is_enabled("#impressiveRadio")
            page.is_disabled("#noRadio")

        time.sleep(3)

    @allure.feature("Функциональность чекбоксов")
    @allure.story("Пользователь может взаимодействовать с чекбоксами")
    @allure.title("Проверка навигации в дереве чекбоксов")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_checkbox(self, page: Page):
        page.goto(DEMOQA_CHECKBOX_LINK)
        with allure.step("Валидация начального состояния"):
            page.get_by_role("treeitem", name="Select Home Home").is_visible()
            page.get_by_role("treeitem", name="Select Desktop Desktop").is_hidden()
        with allure.step("Открытие дерева чекбоксов"):
            page.locator(".rc-tree-switcher").click()
        with allure.step("Валидация, что при открытие появилось дерево с чекбоксами"):
            page.get_by_role("treeitem", name="Select Desktop Desktop").is_visible()

        time.sleep(3)

    @allure.feature("Функциональность динамических элементов")
    @allure.story("Пользователь видит измениня динамических элементов")
    @allure.title("Проверка измений динамических элементов со временем")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.critical
    @pytest.mark.smoke
    @pytest.mark.regression
    def test_dynamic_properties(self, page: Page):

        page.goto(DEMOQA_DYNAMIC_PROPERTIES_LINK)
        with allure.step("Валидация изначального состояния"):
            expect(
                page.get_by_role("button", name="Visible After 5 Seconds")
            ).not_to_be_visible()
            page.get_by_role("button", name="Will enable 5 Seconds").is_disabled()
        with allure.step("Ожидание данимических изменений"):
            page.wait_for_selector("#visibleAfter")
        with allure.step("Валидация изменений динамических элементов"):
            page.get_by_role("button", name="Visible After 5 Seconds").is_visible()
            page.get_by_role("button", name="Will enable 5 Seconds").is_enabled()

        time.sleep(3)

    @allure.feature("Утверждения радио кнопок")
    @allure.story("Валидация состояний радио кнопок")
    @allure.title("Проверка различных утверждений радио кнопок")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.normal
    def test_expect(self, page: Page):
        page.goto(DEMOQA_RADIO_BUTTONS_LINK)
        yes_radio = page.get_by_role("radio", name="Yes")
        impressive_radio = page.get_by_role("radio", name="Impressive")
        no_radio = page.get_by_role("radio", name="No")
        with allure.step("Валидация изначального состояния"):
            expect(no_radio).to_be_disabled()
            expect(yes_radio).to_be_enabled()
            expect(impressive_radio).to_be_enabled()
        with allure.step('Взаимодействие с радио кнопкой "Yes"'):
            page.locator('[for="yesRadio"]').click()
        with allure.step("Валидация обновленного состояния"):
            expect(yes_radio).to_be_checked()
            expect(impressive_radio).not_to_be_checked()

        time.sleep(3)
