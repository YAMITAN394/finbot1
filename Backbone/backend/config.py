import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    google_project_id: str | None = None
    google_credentials: str | None = None

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()