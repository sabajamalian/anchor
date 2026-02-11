"""Database connection and session management.

This module provides database connection setup and session management.
"""

from sqlalchemy import create_engine, text
from sqlalchemy.orm import declarative_base, sessionmaker

from app.config import settings

# Create database engine
engine = create_engine(
    settings.database_url,
    echo=settings.DEBUG,
    pool_pre_ping=True,
)

# Create session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for models
Base = declarative_base()


def get_db():
    """Get database session.
    
    Yields:
        Session: SQLAlchemy database session.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def execute_raw_sql(query: str, params: dict = None):
    """Execute raw SQL query.
    
    Args:
        query: SQL query string.
        params: Optional query parameters.
        
    Returns:
        Result of the query execution.
    """
    with engine.connect() as conn:
        result = conn.execute(text(query), params or {})
        conn.commit()
        return result
