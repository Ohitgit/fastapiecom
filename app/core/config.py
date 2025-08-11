from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str ="postgresql+psycopg2://postgres:password@localhost:5432/invoice" # Change to PostgreSQL if needed

    class Config:
        env_file = ".env"

settings = Settings()
