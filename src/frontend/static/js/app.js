/**
 * Main application JavaScript
 * Handles API interactions and DOM updates
 */

const API_BASE_URL = '/api';

/**
 * Check API health status
 */
async function checkApiHealth() {
    try {
        const response = await fetch('/health');
        const data = await response.json();
        document.getElementById('api-status').textContent = 
            data.status === 'healthy' ? '✓ Healthy' : '✗ Unhealthy';
        document.getElementById('api-status').style.color = 
            data.status === 'healthy' ? 'green' : 'red';
    } catch (error) {
        document.getElementById('api-status').textContent = '✗ Error';
        document.getElementById('api-status').style.color = 'red';
        console.error('API health check failed:', error);
    }
}

/**
 * Check database health status
 */
async function checkDbHealth() {
    try {
        const response = await fetch('/health/db');
        const data = await response.json();
        document.getElementById('db-status').textContent = 
            data.status === 'healthy' ? '✓ Connected' : '✗ Disconnected';
        document.getElementById('db-status').style.color = 
            data.status === 'healthy' ? 'green' : 'red';
    } catch (error) {
        document.getElementById('db-status').textContent = '✗ Error';
        document.getElementById('db-status').style.color = 'red';
        console.error('Database health check failed:', error);
    }
}

/**
 * Load and display all items
 */
async function loadItems() {
    try {
        const response = await fetch(`${API_BASE_URL}/items/`);
        const items = await response.json();
        
        const itemsList = document.getElementById('items-list');
        
        if (items.length === 0) {
            itemsList.innerHTML = '<p>No items found. Create one above!</p>';
            return;
        }
        
        itemsList.innerHTML = items.map(item => `
            <article>
                <header>
                    <strong>${escapeHtml(item.name)}</strong>
                    <button class="secondary outline small" onclick="deleteItem(${item.id})">Delete</button>
                </header>
                <p>${item.description ? escapeHtml(item.description) : '<em>No description</em>'}</p>
                <footer>
                    <small>Created: ${new Date(item.created_at).toLocaleString()}</small>
                </footer>
            </article>
        `).join('');
    } catch (error) {
        document.getElementById('items-list').innerHTML = 
            '<p style="color: red;">Failed to load items</p>';
        console.error('Failed to load items:', error);
    }
}

/**
 * Create a new item
 */
async function createItem(event) {
    event.preventDefault();
    
    const form = event.target;
    const formData = new FormData(form);
    const data = {
        name: formData.get('name'),
        description: formData.get('description')
    };
    
    try {
        const response = await fetch(`${API_BASE_URL}/items/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data)
        });
        
        if (response.ok) {
            form.reset();
            await loadItems();
        } else {
            alert('Failed to create item');
        }
    } catch (error) {
        alert('Error creating item');
        console.error('Failed to create item:', error);
    }
}

/**
 * Delete an item
 */
async function deleteItem(itemId) {
    if (!confirm('Are you sure you want to delete this item?')) {
        return;
    }
    
    try {
        const response = await fetch(`${API_BASE_URL}/items/${itemId}`, {
            method: 'DELETE'
        });
        
        if (response.ok) {
            await loadItems();
        } else {
            alert('Failed to delete item');
        }
    } catch (error) {
        alert('Error deleting item');
        console.error('Failed to delete item:', error);
    }
}

/**
 * Escape HTML to prevent XSS
 */
function escapeHtml(unsafe) {
    return unsafe
        .replace(/&/g, "&amp;")
        .replace(/</g, "&lt;")
        .replace(/>/g, "&gt;")
        .replace(/"/g, "&quot;")
        .replace(/'/g, "&#039;");
}

// Initialize app when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    checkApiHealth();
    checkDbHealth();
    loadItems();
    
    // Set up form submission handler
    document.getElementById('create-item-form').addEventListener('submit', createItem);
    
    // Refresh health status every 30 seconds
    setInterval(() => {
        checkApiHealth();
        checkDbHealth();
    }, 30000);
});
