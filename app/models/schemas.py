"""Pydantic models for request and response data validation."""
from pydantic import BaseModel, Field
from typing import List, Optional


class TextRequest(BaseModel):
    """Request model for text sentiment analysis."""
    text: str = Field(..., min_length=1, description="Text to analyze sentiment")
    

class SentimentResponse(BaseModel):
    """Response model for sentiment analysis."""
    text: str = Field(..., description="Original text that was analyzed")
    sentiment: str = Field(..., description="Sentiment classification (positive, negative, neutral)")
    polarity: float = Field(..., description="Sentiment polarity score (-1 to 1)")
    subjectivity: float = Field(..., description="Subjectivity score (0 to 1)")
    
    
class ErrorResponse(BaseModel):
    """Standard error response model."""
    detail: str = Field(..., description="Error message")
