"""Router configuration for the API."""
from fastapi import APIRouter
from app.api.endpoints import router as sentiment_router

# Create main router
router = APIRouter()

# Include sentiment router
router.include_router(
    sentiment_router,
    prefix="/sentiment",
    tags=["sentiment"],
)
