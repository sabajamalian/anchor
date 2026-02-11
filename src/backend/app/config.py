"""Application configuration.

This module manages application settings and environment variables.
"""

import os

from dotenv import load_dotenv

load_dotenv()


class Settings:
    """Application settings loaded from environment variables."""

    # Database configuration
    DB_SERVER: str = os.getenv("DB_SERVER", "localhost")
    DB_NAME: str = os.getenv("DB_NAME", "anchor_db")
    DB_USER: str = os.getenv("DB_USER", "")
    DB_PASSWORD: str = os.getenv("DB_PASSWORD", "")
    DB_DRIVER: str = os.getenv("DB_DRIVER", "ODBC Driver 18 for SQL Server")

    # Azure Storage configuration
    STORAGE_ACCOUNT_NAME: str = os.getenv("STORAGE_ACCOUNT_NAME", "")
    STORAGE_CONTAINER_NAME: str = os.getenv("STORAGE_CONTAINER_NAME", "uploads")

    # Application configuration
    APP_NAME: str = "Anchor Starter"
    DEBUG: bool = os.getenv("DEBUG", "False").lower() == "true"

    @property
    def database_url(self) -> str:
        """Construct the database connection URL.
        
        Returns:
            str: SQLAlchemy database connection URL.
        """
        if self.DB_USER and self.DB_PASSWORD:
            return (
                f"mssql+pyodbc://{self.DB_USER}:{self.DB_PASSWORD}"
                f"@{self.DB_SERVER}/{self.DB_NAME}"
                f"?driver={self.DB_DRIVER}"
            )
        return (
            f"mssql+pyodbc://{self.DB_SERVER}/{self.DB_NAME}"
            f"?driver={self.DB_DRIVER}&Trusted_Connection=yes"
        )


settings = Settings()
