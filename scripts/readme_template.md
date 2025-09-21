# {{ project_name }}


![Python Version](https://img.shields.io/badge/python-{{ python_version }}-blue.svg)
![Selenium Version](https://img.shields.io/badge/selenium-{{ selenium_version }}-green.svg)


## 📖 Описание

{{ description }}

## ⚙️ Предварительные требования

*   Python {{ python_version }} или выше
*   Браузер {{ browser_name }} (или другой, совместимый с WebDriver)
*   Установленный WebDriver (можно установить автоматически с помощью [webdriver-manager](https://pypi.org/project/webdriver-manager/))

## 🚀 Установка

1.  Клонируйте репозиторий:
    ```bash
    git clone https://github.com/{{ github_username }}/{{ project_name }}.git
    cd {{ project_name }}
    ```

2.  Создайте виртуальное окружение и активируйте его:
    ```bash
    python -m venv venv
    source venv/bin/activate  # для Linux/MacOS
    # или
    venv\Scripts\activate     # для Windows
    ```

3.  Установите зависимости:
    ```bash
    pip install -r requirements.txt
    ```

## 💻 Использование

Тесты находятся  в пакете `tests`.

Запуск тестов командой:
```bash
 pytest tests/ -s -v
 ```



## 🤝 Зависимости
Основные зависимости:
{% for dep in dependencies %}

{{ dep }}
{% endfor %}

Полный список смотрите в файле requirements.txt.

## 👤 Автор
{{ author_name }}

Email: {{ author_email }}

GitHub: [@{{ github_username }}](https://github.com/{{ github_username }})