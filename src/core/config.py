from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Cover Letter Generation Service"
    API_V1_STR: str = "/api/v1"

settings = Settings()