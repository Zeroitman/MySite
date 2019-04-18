from behave import given, when, then
from time import sleep


@given(u'Я открыл страницу "Входа"')
def open_login_page(context):
    sleep(1)
    context.browser.get('http://localhost:8000/auth/login/')


@when(u'Я ввожу текст "{text}" в поле "{name}"')
def enter_text(context, text, name):
    sleep(1)
    context.browser.find_element_by_name(name).send_keys(text)


@when(u'Я отправляю форму')
def submit_form(context):
    sleep(1)
    context.browser.find_element_by_css_selector('button').click()


@then(u'Я должен быть на главной странице')
def should_be_at_main(context):
    sleep(1)
    assert context.browser.current_url == 'http://localhost:8000/'


@then("Я должен быть на странице входа")
def should_be_at_login(context):
    sleep(1)
    assert context.browser.current_url == 'http://localhost:8000/auth/login/'


@then('Я должен видеть сообщение об ошибке с текстом "{text}"')
def see_error_with_text(context, text):
    sleep(1)
    error = context.browser.find_element_by_css_selector('.form-text.text-danger')
    assert error.text == text
