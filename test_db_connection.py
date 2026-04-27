from sqlalchemy import create_engine, text

from settings import settings

try:
    print(f"Пытаюсь подключиться к: {settings.sqlalchemy_url}")
    engine = create_engine(settings.sqlalchemy_url, echo=True)
    with engine.connect() as conn:
        result = conn.execute(text("SELECT 1"))
        print(f"Подключение успешно! Результат: {result.scalar()}")
except Exception as e:
    print(f"Ошибка: {type(e).__name__}: {e}")