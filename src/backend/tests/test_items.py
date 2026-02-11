"""Tests for items endpoints."""

import pytest


def test_list_items_empty(client):
    """Test listing items when database is empty.
    
    Args:
        client: Test client fixture.
    """
    response = client.get("/api/items/")
    assert response.status_code == 200
    assert response.json() == []


def test_create_item(client):
    """Test creating a new item.
    
    Args:
        client: Test client fixture.
    """
    item_data = {
        "name": "Test Item",
        "description": "Test Description"
    }
    response = client.post("/api/items/", json=item_data)
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == item_data["name"]
    assert data["description"] == item_data["description"]
    assert "id" in data


def test_get_item(client):
    """Test getting a specific item.
    
    Args:
        client: Test client fixture.
    """
    # Create an item first
    item_data = {"name": "Test Item", "description": "Test Description"}
    create_response = client.post("/api/items/", json=item_data)
    item_id = create_response.json()["id"]
    
    # Get the item
    response = client.get(f"/api/items/{item_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == item_id
    assert data["name"] == item_data["name"]


def test_get_item_not_found(client):
    """Test getting a non-existent item.
    
    Args:
        client: Test client fixture.
    """
    response = client.get("/api/items/999")
    assert response.status_code == 404


def test_update_item(client):
    """Test updating an item.
    
    Args:
        client: Test client fixture.
    """
    # Create an item first
    item_data = {"name": "Original Name", "description": "Original Description"}
    create_response = client.post("/api/items/", json=item_data)
    item_id = create_response.json()["id"]
    
    # Update the item
    updated_data = {"name": "Updated Name", "description": "Updated Description"}
    response = client.put(f"/api/items/{item_id}", json=updated_data)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == updated_data["name"]
    assert data["description"] == updated_data["description"]


def test_delete_item(client):
    """Test deleting an item.
    
    Args:
        client: Test client fixture.
    """
    # Create an item first
    item_data = {"name": "Test Item", "description": "Test Description"}
    create_response = client.post("/api/items/", json=item_data)
    item_id = create_response.json()["id"]
    
    # Delete the item
    response = client.delete(f"/api/items/{item_id}")
    assert response.status_code == 204
    
    # Verify it's deleted
    get_response = client.get(f"/api/items/{item_id}")
    assert get_response.status_code == 404


def test_create_item_without_description(client):
    """Test creating an item without description.
    
    Args:
        client: Test client fixture.
    """
    item_data = {"name": "Test Item"}
    response = client.post("/api/items/", json=item_data)
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == item_data["name"]
    assert data["description"] is None
