from pydantic_settings import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    MONGODB_URL: str = "mongodb://localhost:27017"
    DATABASE_NAME: str = "finance_dashboard"
    SECRET_KEY: str = "supersecretkey"
    ALLOWED_ORIGINS: str = "http://localhost:3000,http://127.0.0.1:3000"
    # Allow all Vercel preview/production domains by default; can be overridden via env
    ALLOWED_ORIGIN_REGEX: str | None = "https://.*vercel\\.app"

    @property
    def allowed_origins_list(self) -> list[str]:
        return [o.strip() for o in self.ALLOWED_ORIGINS.split(",")]

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


@lru_cache()
def get_settings() -> Settings:
    return Settings()
