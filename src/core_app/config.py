import os

class Settings:
    APP_NAME: str = "Smart Campus Core Business Service"
    APP_ENV: str = os.getenv("APP_ENV", "local")
    AUTH_TOKEN_SECRET: str = os.getenv("AUTH_TOKEN_SECRET", "lab-token-b6-secret")

settings = Settings()