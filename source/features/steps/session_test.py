from behave import given, when, then
from time import sleep


@when(u'Я нажимаю на кнопку "Начать сессию"')
def session_create(context):
    sleep(1)
    context.browser.find_element_by_id('start_session').click()


@then(u'Я должен быть на странице проведения сессии')
def check_session_page(context):
    sleep(1)
    assert context.get_url('http://localhost:8000/program/<int:pk>/session')


@then(u'Я нажимаю кнопки')
def press_button(context):
    sleep(1)
    context.browser.find_element_by_id('but_2').click()
    context.browser.find_element_by_id('but_1').click()


@then(u'Я перехожу к результатам сессии')
def finish_session(context):
    sleep(1)
    context.browser.find_element_by_id('session_result').click()


@then(u'Я закрываю сессию')
def close_session(context):
    sleep(1)
    context.browser.find_element_by_id('session_close').click()
