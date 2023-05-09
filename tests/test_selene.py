"""Указываем в настройках Modify Run Configuration/Additional Arguments :
--alluredir=allure-results
1. Установил scoop в PowerShell через терминал
2. Команда для запуска отчета allure serve tests/allure-results
3. При запуске нового теста, удаляем старые результаты, иначе показывается не верные данные
4. Запускаем тест и вручную указываем чтобы сохранил результаты в отчет pytest -s -v --alluredir=tests/allure-results
5. Чтобы увидеть отчет, вбиваем команду allure serve tests/allure-results
"""


from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


# def test_github():
#     browser.open("https://github.com")
#
#     s(".header-search-input").click()
#     s(".header-search-input").send_keys("eroshenkoam/allure-example")
#     s(".header-search-input").submit()
#
#     s(by.link_text("eroshenkoam/allure-example")).click()
#     s('#issues-tab').click()
#
#     s(by.partial_text('#76')).should(be.visible)#ищем по тексту по частично,не полная фраза