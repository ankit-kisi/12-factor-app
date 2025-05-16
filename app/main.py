import uvicorn
from fastapi import FastAPI
from app.core.config import settings
from app.api.routes import router as api_router
from app.core.middleware import setup_middleware
from app.core.logging_config import setup_logging

def create_application() -> FastAPI:
    """Create FastAPI application."""
    # Set up logging
    setup_logging()
    
    application = FastAPI(
        title=settings.APP_NAME,
        debug=settings.DEBUG,
        version="0.1.0",
        description="Text Sentiment Analysis API built following 12-factor app principles"
    )

    # Set up middleware
    setup_middleware(application)

    # Include API router
    application.include_router(api_router, prefix=settings.API_V1_STR)

    return application

app = create_application()

@app.get("/")
async def root():
    """Root endpoint."""
    return {
        "message": "Text Sentiment Analysis API",
        "docs_url": f"{settings.API_V1_STR}/docs",
    }

if __name__ == "__main__":
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0", 
        port=8000,
        reload=settings.DEBUG
    )
