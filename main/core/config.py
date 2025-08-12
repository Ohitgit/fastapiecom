from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str ="postgresql+psycopg2://postgres:password@localhost:5432/flowvascular"


    class Config:
         pass

settings = Settings()
