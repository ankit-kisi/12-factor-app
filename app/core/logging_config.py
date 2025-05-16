"""Logging configuration for the application."""
import logging
import sys
from typing import Dict, Any

from app.core.config import settings


def get_logging_config() -> Dict[str, Any]:
    """Return the logging configuration dictionary."""
    log_level = settings.LOG_LEVEL.upper()
    
    return {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "default": {
                "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
                "datefmt": "%Y-%m-%d %H:%M:%S",
            },
        },
        "handlers": {
            "console": {
                "level": log_level,
                "class": "logging.StreamHandler",
                "formatter": "default",
                "stream": sys.stdout,
            },
        },
        "loggers": {
            "app": {"handlers": ["console"], "level": log_level, "propagate": False},
            "uvicorn": {"handlers": ["console"], "level": log_level, "propagate": False},
            "fastapi": {"handlers": ["console"], "level": log_level, "propagate": False},
        },
    }


def setup_logging():
    """Configure logging based on the settings."""
    log_level = getattr(logging, settings.LOG_LEVEL.upper())
    logging.basicConfig(
        level=log_level,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
