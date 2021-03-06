Feature: Тест на начало сессии(CRUD)

  Scenario: Начало сессии
    Given Я открыл страницу "Входа"
    When Я ввожу текст "admin" в поле "username"
    When Я ввожу текст "admin" в поле "password"
    Then Я отправляю форму
    Then Я должен быть на главной странице
    When Я нажимаю на кнопку "Начать сессию"
    Then Я должен быть на странице проведения сессии
    Then Я нажимаю кнопки
    Then Я перехожу к результатам сессии
    Then Я закрываю сессию

  Scenario: Сессия без вводы ответов
    Given Я открыл страницу "Входа"
    When Я ввожу текст "admin" в поле "username"
    When Я ввожу текст "admin" в поле "password"
    Then Я отправляю форму
    Then Я должен быть на главной странице
    When Я нажимаю на кнопку "Начать сессию"
    Then Я должен быть на странице проведения сессии
    Then Я перехожу к результатам сессии
    Then Я закрываю сессию




