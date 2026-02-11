"""Health check router.

This module provides health check endpoints.
"""

from fastapi import APIRouter, Depends
from sqlalchemy import text
from sqlalchemy.orm import Session

from app.database.connection import get_db

router = APIRouter()


@router.get("/health")
async def health_check():
    """Basic health check endpoint.
    
    Returns:
        dict: Health status.
    """
    return {"status": "healthy", "service": "anchor-api"}


@router.get("/health/db")
async def database_health_check(db: Session = Depends(get_db)):
    """Database health check endpoint.
    
    Args:
        db: Database session.
        
    Returns:
        dict: Database health status.
    """
    try:
        # Execute a simple query to check database connectivity
        db.execute(text("SELECT 1"))
        return {"status": "healthy", "database": "connected"}
    except Exception as e:
        return {"status": "unhealthy", "database": "disconnected", "error": str(e)}
