from behave import then, when
from time import sleep

from selenium.webdriver.support.select import Select


@then(u'Я перехожу на страницу "Программы"')
def open_program_page(context):
    sleep(5)
    context.browser.get('http://localhost:8000/program')

@then(u'Нажимаю на кнопку "Добавление программы"')
def program_create(context):
    sleep(1)
    context.browser.find_element_by_id('program_add').click()

@then(u'Я должен быть на странице "Добавление программы"')
def check_program_page(context):
    sleep(1)
    assert context.browser.current_url == 'http://localhost:8000/program/create'


@then(u'Выбираем ребенка в программе')
def choice_child_program(context):
    sleep(1)
    Select(context.browser.find_element_by_id("id_child")).select_by_visible_text("2. Кошкин Василий")

@then(u'Выбираем тераписта для ребенка в программе')
def choice_therapist_for_child_program(context):
    sleep(1)
    Select(context.browser.find_element_by_id("id_author_therapist")).select_by_visible_text("4. Терапист1 Тест")

@then(u'Выбираем навык для ребенка в программе')
def choice_skill(context):
    sleep(1)
    context.browser.find_element_by_xpath(
        u"(.//*[normalize-space(text()) and normalize-space(.)='Навыки:'])[1]/following::option[2]").click()

@then(u'Нажимаем на сохранение')
def click_save(context):
    sleep(1)
    context.browser.find_element_by_xpath(
        u"(.//*[normalize-space(text()) and normalize-space(.)='Навыки:'])[1]/following::button[1]").click()


