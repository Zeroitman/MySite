Feature: Тест на добавление программ

  Scenario: Добавление программы
    Then Я перехожу на страницу "Программы"
    Then Нажимаю на кнопку "Добавление программы"
    Then Я ввожу текст "abrakadabra" в поле "name"
    Then Я ввожу текст "some description" в поле "description"
    Then Я ввожу текст "some comment" в поле "program_comment"
    Then Я должен быть на странице "Добавление программы"
    Then Выбираем ребенка в программе
    Then Выбираем тераписта для ребенка в программе
    Then Выбираем навык для ребенка в программе
    Then Нажимаем на сохранение
