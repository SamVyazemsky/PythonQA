import pytest
from selenium import webdriver
from selenium.webdriver import ChromeOptions


def test_otus(prepare_test):
    """
    My First Test
    """
    # Открываем браузер
    browser = webdriver.Chrome()
    # Переходим на сайт otus.ru
    browser.get("https://otus.ru/")
    # Проверяем титл страницы
    page_title = browser.title
    assert page_title == "Онлайн‑курсы для профессионалов, дистанционное обучение современным профессиям"


@pytest.fixture()
def prepare_test():
    # Открываем браузер
    browser = webdriver.Chrome()

    return browser

