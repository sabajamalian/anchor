"""Items router.

This module provides CRUD operations for items resource.
"""

from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel, ConfigDict
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.models.item import Item

router = APIRouter()


class ItemCreate(BaseModel):
    """Schema for creating an item.
    
    Attributes:
        name: Item name.
        description: Item description (optional).
    """
    name: str
    description: str | None = None


class ItemResponse(BaseModel):
    """Schema for item response.
    
    Attributes:
        id: Item ID.
        name: Item name.
        description: Item description.
        created_at: Creation timestamp.
        updated_at: Last update timestamp.
    """
    id: int
    name: str
    description: str | None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


@router.get("/", response_model=list[ItemResponse])
async def list_items(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    """List all items.
    
    Args:
        skip: Number of items to skip.
        limit: Maximum number of items to return.
        db: Database session.
        
    Returns:
        List[ItemResponse]: List of items.
    """
    items = db.query(Item).offset(skip).limit(limit).all()
    return items


@router.get("/{item_id}", response_model=ItemResponse)
async def get_item(item_id: int, db: Session = Depends(get_db)):
    """Get a specific item by ID.
    
    Args:
        item_id: Item ID.
        db: Database session.
        
    Returns:
        ItemResponse: The requested item.
        
    Raises:
        HTTPException: If item is not found.
    """
    item = db.query(Item).filter(Item.id == item_id).first()
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@router.post("/", response_model=ItemResponse, status_code=201)
async def create_item(item_data: ItemCreate, db: Session = Depends(get_db)):
    """Create a new item.
    
    Args:
        item_data: Item creation data.
        db: Database session.
        
    Returns:
        ItemResponse: The created item.
    """
    item = Item(name=item_data.name, description=item_data.description)
    db.add(item)
    db.commit()
    db.refresh(item)
    return item


@router.put("/{item_id}", response_model=ItemResponse)
async def update_item(
    item_id: int,
    item_data: ItemCreate,
    db: Session = Depends(get_db)
):
    """Update an existing item.
    
    Args:
        item_id: Item ID.
        item_data: Updated item data.
        db: Database session.
        
    Returns:
        ItemResponse: The updated item.
        
    Raises:
        HTTPException: If item is not found.
    """
    item = db.query(Item).filter(Item.id == item_id).first()
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")

    item.name = item_data.name
    item.description = item_data.description
    db.commit()
    db.refresh(item)
    return item


@router.delete("/{item_id}", status_code=204)
async def delete_item(item_id: int, db: Session = Depends(get_db)):
    """Delete an item.
    
    Args:
        item_id: Item ID.
        db: Database session.
        
    Raises:
        HTTPException: If item is not found.
    """
    item = db.query(Item).filter(Item.id == item_id).first()
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")

    db.delete(item)
    db.commit()
    return None
