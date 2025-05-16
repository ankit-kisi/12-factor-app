"""API routes for the application."""
from fastapi import APIRouter, HTTPException, Depends
from app.models.schemas import TextRequest, SentimentResponse, ErrorResponse
from app.services.sentiment import sentiment_service
import logging

# Create logger
logger = logging.getLogger(__name__)

# Create router
router = APIRouter()

@router.post(
    "/sentiment",
    response_model=SentimentResponse,
    responses={
        400: {"model": ErrorResponse, "description": "Bad request"},
        500: {"model": ErrorResponse, "description": "Internal server error"},
    },
    summary="Analyze text sentiment",
    description="Analyzes the sentiment of the given text and returns sentiment classification, polarity, and subjectivity scores.",
)
async def analyze_sentiment(request: TextRequest):
    """Analyze sentiment of the provided text."""
    try:
        logger.info(f"Received sentiment analysis request")
        result = sentiment_service.analyze_text(request.text)
        return result
    except ValueError as e:
        logger.warning(f"Bad request: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logger.error(f"Error processing request: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")


@router.get(
    "/health",
    summary="Health check endpoint",
    description="Returns the status of the API",
)
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy"}
