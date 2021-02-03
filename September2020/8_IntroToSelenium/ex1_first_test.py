import pytest
from selenium import webdriver


def test_otus():
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
