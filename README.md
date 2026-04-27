# Настройка проекта Cookbook
Клонирование репозитория
```bash
git clone https://github.com/sansentrailles/cookbook.git
```

Открыть проект в редакторе, в корне проект создать файл `.env` и добавить следующие переменные:
```
POSTGRES_USER=postgres
POSTGRES_PASSWORD=123123
POSTGRES_DB=cookbookdb
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
```

Для создания виртуального окружения и установки библиотек:
```bash
poetry install
```

Для активации виртуального окружения:
```bash
poetry env activate
```

Запуск Postgres
```bash
docker compose -f "docker-compose.dev.yml" up -d
```

Применить миграции:
```bash
alembic upgrade head
```

Запуск приложениея:
```bash
python cookbook/main.py
```

API будет доступен в браузреер по адресу `https://127.0.0.1/docs`
