from urllib.parse import quote_plus

from settings import settings

print(f"User: '{settings.postgres_user}'")
print(f"Password: '{settings.postgres_password}'")
print(f"Password bytes: {settings.postgres_password.encode('utf-8')}")
print(f"Host: '{settings.postgres_host}'")
print(f"Port: {settings.postgres_port}")
print(f"DB: '{settings.postgres_db}'")
print(f"SQLAlchemy URL: {settings.sqlalchemy_url}")

# Проверим кодировку
import sys

print(f"Default encoding: {sys.getdefaultencoding()}")
print(f"Filesystem encoding: {sys.getfilesystemencoding()}")