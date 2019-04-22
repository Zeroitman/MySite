# Applied Behavior Analysis

Applied Behavior Analysis Project - это проект прикладного анализа поведения для детей с отклонениями в поведении.
Прикладной анализ поведения — это научная дисциплина, которая предполагает использование современной поведенческой теории научения для изменения поведения. 

## Установка

Ссылка на репозиторий [BitBucket](https://bitbucket.org/abapythonteam/aba/src/master/)

Установите python на ваш пк [Python](https://www.python.org/downloads/).
Установите пакет менеджер [pip](https://pip.pypa.io/en/stable/).
После установки пакет менеджера [pip](https://pip.pypa.io/en/stable/), создайте папку проекта, перейдите в неё для установки всех зависимостей.
Виртуальное окружение в Python создаётся с помощью специального пакета virtualenv. 

Установка:

В Windows:

```bash
pip install virtualenv
```

Linux и Mac OS:

```bash
sudo pip install virtualenv
```

После установки проверьте версию виртуального окружения:

```bash
virtualenv --version
```

В папке проекта пропишите в консоли команду для установки виртуального окружения:

```bash
virtualenv -p python3 venv
```

После установки можно будет активировать виртуальное окружение:
Windows:

```bash
venv\Scripts\activate
```

Linux и Mac OS:

```bash
. venv/bin/activate
```

Чтобы отключить (деактивировать) виртуальное окружение, в корневой папке используйте команду deactivate:

```bash
(venv) корневая папка > deactivate
```

Установите Django:

```bash
pip install Django
```
 
 Склонируйте проект:

 ```bash
 git clone https://Maks941@bitbucket.org/abapythonteam/aba.git
```

После установки перейдите в папку с файлом manage.py и проведите миграции:

```bash
python3 manage.py makemigration
python3 manage.py migrate
```
Создайте супер юзера:

```bash
python3 manage.py createsuperuser
```

Загрузите файлы из json файла из папки dumpdata:

```bash
python3 manage.py loaddata /Путь до файла/dump.json
```

Установите все зависимости проекта:

```bash
pip install -r requirements.txt
```
В папке с manage.py запустите проект:

```bash
python3 manage.py runserver
```








