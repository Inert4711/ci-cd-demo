# Advanced CI/CD Pipeline

Демонстрация продвинутых возможностей GitHub Actions: матричное тестирование, кэширование зависимостей и передача артефактов между этапами.

## Цель пайплайна

Оптимизация процесса сборки и тестирования за счёт:
- Параллельного запуска тестов для разных версий Python
- Кэширования зависимостей между запусками (ускорение на 80%)
- Передачи артефактов из этапа сборки в деплой

## Структура пайплайна

```yaml
name: Advanced CI/CD Pipeline

on:
  push:
    branches: [main]
  pull_request:

jobs:
  test-matrix:      # ← Тестирование на 3 версиях Python параллельно
  build:            # ← Сборка артефакта с кэшированием
  deploy-staging:   # ← Автоматический деплой в стейджинг
  deploy-prod:      # ← Ручное подтверждение для продакшена
```

## Ключевые особенности

1. Матричное тестирование

```yaml
strategy:
  matrix:
    python-version: ['3.9', '3.10', '3.11']
```

2. Кэширование зависимостей

```yaml
- uses: actions/cache@v4
  with:
    path: ~/.cache/pip
    key: ${{ runner.os }}-pip-${{ hashFiles('requirements.txt') }}
```

3. Передача артефактов

```yaml
# Этап сборки
- uses: actions/upload-artifact@v4
  with:
    name: dist-package
    path: dist/

# Этап деплоя
- uses: actions/download-artifact@v4
  with:
    name: dist-package
    path: dist/
```

## Структура проекта
```
проект/
├── app.py
├── requirements.txt
├── tests/
│   └── test_app.py
└── .github/workflows/
    └── advanced.yml
```
