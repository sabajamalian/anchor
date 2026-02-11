"""Item model.

This module defines the Item model for the database.
"""

from sqlalchemy import Column, Integer, String, DateTime, func
from app.database.connection import Base


class Item(Base):
    """Item model representing items in the database.
    
    Attributes:
        id: Primary key.
        name: Item name.
        description: Item description.
        created_at: Timestamp when the item was created.
        updated_at: Timestamp when the item was last updated.
    """
    
    __tablename__ = "items"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    description = Column(String(1000), nullable=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
