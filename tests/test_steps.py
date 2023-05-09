import allure
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s

"""1. Добавляем шаги в тест при помощи with allure.step.
 --- шаги отображаются в отчете"""

"""Первый подход использования allure
 --- with allure.step()"""
def test_dynamic_steps():
    with allure.step("Открываем главную страницу"):
        browser.open("https://github.com")

    with allure.step("Ищем репозиторий"):
        s(".header-search-input").click()
        s(".header-search-input").send_keys("eroshenkoam/allure-example")
        s(".header-search-input").submit()

    with allure.step("Переходим по ссылке репозитория"):
        s(by.link_text("eroshenkoam/allure-example")).click()
        s('#issues-tab').click()

    with allure.step("Проверяем наличие Issue с номером 76"):
        s(by.partial_text('#76')).should(be.visible)#ищем по тексту по частично,не полная фраза


#------------------------------------------------------#
#------------------------------------------------------#
#------------------------------------------------------#

"""Разбили шаги по декараторам @allure.step(''), написали тестовую функцию 
 def test_decorator_steps() и добавили в нее шаги в виде функций """

"""Второй подход с allure
Используем декоратор и позже все шаги прописываем в одну функцию
@allure.step()"""

def test_decorator_steps():
    open_main_page()
    search_for_repository("eroshenkoam/allure-example")
    go_to_repository("eroshenkoam/allure-example")
    open_issue_tab()
    should_see_issue_with_number("#76")



@allure.step("Открываем главную страницу")
def open_main_page():
    browser.open("https://github.com")

@allure.step("Ищем репозиторий {repo}")
def search_for_repository(repo):
    s(".header-search-input").click()
    s(".header-search-input").send_keys(repo)
    s(".header-search-input").submit()

@allure.step("Переходим по ссылке репозитория {repo}")
def go_to_repository(repo):
    s(by.link_text(repo)).click()
    s('#issues-tab').click()

@allure.step("Открываем таб Issues")
def open_issue_tab():
    s('#issues-tab').click()

@allure.step("Проверяем наличие Issue с номером {number}")
def should_see_issue_with_number(number):
    s(by.partial_text(number)).click()