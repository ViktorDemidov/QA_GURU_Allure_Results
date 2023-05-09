import allure
from allure_commons.types import Severity

def test_dynamic_labels():
    allure.dynamic.tag("web")
    allure.dynamic.severity(Severity.BLOCKER)
    allure.dynamic.feature("Задачи в репозитории")#в отчете будет отображаться в фильтрах Behaviors
    allure.dynamic.story("неавторизованный пользователь не может создать задачу в репозитории")#в отчете будет отображаться в фильтрах Behaviors
    allure.dynamic.link("https://github.com", name="Testing")



"""ВОТ ТАКОЙ ПРАВИЛЬНЫЙ ПОДХОД"""
@allure.tag("critical")
@allure.severity(Severity.CRITICAL)#редко используется
@allure.label("owner", "eroshenkoam")
@allure.feature("Задача в репозитории")
@allure.story("Авторизованный пользователь может создать задачу в репозитории")
@allure.link("https://github.com", name="Testing")
def test_decorator_labels():
    pass