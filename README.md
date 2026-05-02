# PNID — CI/CD Demo Project

Демонстраційний Python-проєкт з 5 GitHub Actions workflows.

## Структура проєкту

```
├── app/
│   ├── __init__.py
│   └── calculator.py        # Модуль калькулятора
├── tests/
│   ├── __init__.py
│   └── test_calculator.py   # Pytest-тести
├── .github/workflows/
│   ├── 1_pytest.yml          # Автоматичне тестування
│   ├── 2_linting.yml         # Перевірка стилю коду
│   ├── 3_multiversion.yml    # Мультиверсійне тестування
│   ├── 4_docker.yml          # Збірка Docker-контейнера
│   └── 5_html_report.yml     # HTML-звіт
├── Dockerfile
├── requirements.txt
├── setup.cfg
└── .gitignore
```

## GitHub Actions Workflows

| # | Workflow | Опис |
|---|---------|------|
| 1 | **Pytest Tests** | Автоматичний запуск тестів з Pytest |
| 2 | **Code Linting** | Перевірка стилю коду з Flake8 |
| 3 | **Multi-version Testing** | Тестування на Python 3.9 / 3.10 / 3.11 / 3.12 |
| 4 | **Docker Build** | Збірка Docker-образу та запуск тестів у контейнері |
| 5 | **HTML Test Report** | Генерація HTML-звіту тестування |

## Локальний запуск

```bash
pip install -r requirements.txt
python -m pytest tests/ -v
```
