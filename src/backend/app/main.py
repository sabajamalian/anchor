"""Main FastAPI application entry point.

This module initializes the FastAPI application and configures routes.
"""

from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

from app.routers import health, items

app = FastAPI(
    title="Anchor Starter API",
    description="A starter template for FastAPI applications with Azure",
    version="1.0.0"
)

# Include routers
app.include_router(health.router, tags=["health"])
app.include_router(items.router, prefix="/api/items", tags=["items"])

# Mount static files and templates
static_path = Path(__file__).parent.parent.parent / "frontend" / "static"
templates_path = Path(__file__).parent.parent.parent / "frontend" / "templates"

if static_path.exists():
    app.mount("/static", StaticFiles(directory=str(static_path)), name="static")


@app.get("/", response_class=HTMLResponse)
async def read_root():
    """Serve the main HTML page.
    
    Returns:
        HTMLResponse: The main index page.
    """
    index_file = templates_path / "index.html"
    if index_file.exists():
        return HTMLResponse(content=index_file.read_text())
    return HTMLResponse(content="<h1>Welcome to Anchor Starter API</h1>")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
