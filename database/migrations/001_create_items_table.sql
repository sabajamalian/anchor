-- Migration: 001 - Create items table
-- Description: Initial schema for items resource
-- Date: 2026-02-11

-- Create items table
CREATE TABLE items (
    id INT IDENTITY(1,1) PRIMARY KEY,
    name NVARCHAR(255) NOT NULL,
    description NVARCHAR(1000),
    created_at DATETIME2 DEFAULT GETDATE(),
    updated_at DATETIME2 DEFAULT GETDATE()
);

-- Create index on name for faster lookups
CREATE INDEX idx_items_name ON items(name);

-- Create trigger for updating updated_at timestamp
CREATE TRIGGER trg_items_update
ON items
AFTER UPDATE
AS
BEGIN
    SET NOCOUNT ON;
    UPDATE items
    SET updated_at = GETDATE()
    FROM items i
    INNER JOIN inserted ins ON i.id = ins.id;
END;
GO
