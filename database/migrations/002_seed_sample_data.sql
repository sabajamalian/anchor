-- Migration: 002 - Seed sample data
-- Description: Insert sample items for testing
-- Date: 2026-02-11

-- Insert sample items
INSERT INTO items (name, description) VALUES
('Sample Item 1', 'This is a sample item for testing the API'),
('Sample Item 2', 'Another sample item with a different description'),
('Sample Item 3', 'A third sample item to demonstrate the list view');
