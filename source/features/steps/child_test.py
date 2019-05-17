from behave import given, when, then
from time import sleep


@then(u'Я перехожу на страницу ”Дети”')
def open_child_page(context):
    sleep(1)
    context.browser.find_element_by_id('child_page').click()


@then(u'Я должен быть на странице ”Дети”')
def check_child_page(context):
    sleep(1)
    assert context.browser.current_url == 'http://localhost:8000/child/'


@when(u'Я нажимаю на кнопку "Добавить ребенка"')
def child_create(context):
    sleep(1)
    context.browser.find_element_by_id('child_add').click()


@then(u'Я должен быть на странице добавления ребенка')
def check_child_add_page(context):
    sleep(1)
    assert context.browser.current_url == 'http://localhost:8000/child/create'


@then(u'Я добавляю ребенка')
def send_child_form(context):
    sleep(1)
    context.browser.find_element_by_id('add_child_button').click()


@then(u'Я должен оказаться в профиле ребенка')
def check_child_profile(context):
    sleep(1)
    assert context.get_url('http://localhost:8000/child/<int:pk>')
