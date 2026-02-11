"""Tests for health check endpoints."""

import pytest


def test_health_check(client):
    """Test basic health check endpoint.
    
    Args:
        client: Test client fixture.
    """
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert data["service"] == "anchor-api"


def test_database_health_check(client):
    """Test database health check endpoint.
    
    Args:
        client: Test client fixture.
    """
    response = client.get("/health/db")
    assert response.status_code == 200
    data = response.json()
    assert "status" in data
    assert "database" in data
