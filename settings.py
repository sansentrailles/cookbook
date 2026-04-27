from urllib.parse import quote_plus

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    postgres_user: str
    postgres_password: str
    postgres_db: str
    postgres_host: str
    postgres_port: int

    @property
    def sqlalchemy_url(self) -> str:
        return (f"postgresql+psycopg2://{self.postgres_user}:{self.postgres_password}"
                f"@{self.postgres_host}:{self.postgres_port}/{self.postgres_db}"
                f"?client_encoding=utf8")

    @property
    def database_url(self) -> str:
        return (f"postgresql+asyncpg://{self.postgres_user}:{self.postgres_password}"
                f"@{self.postgres_host}:{self.postgres_port}/{self.postgres_db}")
    
    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()