import pytest
import allure
import time
from playwright.sync_api import Page, sync_playwright

from constants import EXAMPLE_LINK, GOOGLE_LINK, WIKIPEDIA_LINK, YANDEX_LINK


@allure.epic("Работа с playwright")
@allure.label("qa_name", "Ivan Petrovich")
@allure.tag("ui")
@allure.title("Примеры работы с playwright")
@pytest.mark.ui
class TestPlaywright:
    """Класс с примерами работы с playwright"""

    @allure.feature("Открытие нескольких страниц")
    @allure.title("Открытие нескольких страниц в двух контекстах одновременно")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.normal
    def test_some_entities(self):
        """Тест открытия браузера в двух контекстах"""
        with allure.step(
            "Инициализация playwright и открытие браузера в двух контекстах"
        ):
            with sync_playwright() as p:
                browser1 = p.chromium.launch(headless=False)

                context1_1 = browser1.new_context()
                context1_2 = browser1.new_context()

                page1_1_1 = context1_1.new_page()
                page1_1_2 = context1_1.new_page()
                page1_2_1 = context1_2.new_page()
                page1_2_2 = context1_2.new_page()

                page1_1_1.goto(EXAMPLE_LINK)
                page1_1_2.goto(GOOGLE_LINK)
                page1_2_1.goto(WIKIPEDIA_LINK)
                page1_2_2.goto(YANDEX_LINK)

                time.sleep(10)
            with allure.step("Закрытие страниц"):
                page1_1_1.close()
                page1_1_2.close()
                page1_2_1.close()
                page1_2_2.close()
            with allure.step("Закрытие контекстов"):
                context1_1.close()
                context1_2.close()
            with allure.step("Закрытие браузера"):
                browser1.close()

    @allure.story("Тестирование двух браузеров одновременно")
    @allure.title("Тестирование открытия двух разных браузеров одновренно")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.normal
    def test_multiple_browsers(self):
        """Тест открытия двух разных браузеров одновременно"""
        with allure.step("Инициализация playwright и открытие браузеров"):
            with sync_playwright() as p:
                chromium_browser = p.chromium.launch(headless=False)
                firefox_browser = p.firefox.launch(headless=False)

                chromium_page = chromium_browser.new_page()
                firefox_page = firefox_browser.new_page()

                chromium_page.goto(EXAMPLE_LINK)
                firefox_page.goto(GOOGLE_LINK)

                time.sleep(10)
            with allure.step("Закритие браузеров"):
                chromium_browser.close()
                firefox_browser.close()
