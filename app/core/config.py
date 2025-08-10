from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql+psycopg2://postgres:12345@localhost:5432/ecomerce"  # Change to PostgreSQL if needed

    class Config:
        env_file = ".env"

settings = Settings()
