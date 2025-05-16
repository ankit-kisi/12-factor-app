"""Settings for the application following 12-factor app principles."""
from pydantic import BaseSettings
from typing import List


class Settings(BaseSettings):
    """Application settings.
    
    Following the 12-factor app methodology, configuration is stored in environment variables.
    """
    # General settings
    APP_NAME: str = "sentiment-analysis-api"
    ENV: str = "development"
    DEBUG: bool = False
    LOG_LEVEL: str = "info"
    
    # API settings
    API_V1_STR: str = "/api/v1"
    
    # CORS settings
    ALLOWED_ORIGINS: List[str] = ["http://localhost:8000", "http://localhost:3000"]
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True


# Create settings instance
settings = Settings()
