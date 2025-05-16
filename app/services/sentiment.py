"""Sentiment analysis services."""
import logging
from textblob import TextBlob
import nltk
from typing import Dict, Any


logger = logging.getLogger(__name__)


class SentimentAnalysisService:
    """Service for analyzing text sentiment."""
    
    def __init__(self):
        """Initialize the service and download required NLTK data."""
        try:
            # Download necessary NLTK data for TextBlob
            logger.info("Checking NLTK data...")
            nltk.download('punkt', quiet=True)
        except Exception as e:
            logger.error(f"Error downloading NLTK data: {e}")
            # Continue even if download fails, as the data might already be available
    
    def analyze_text(self, text: str) -> Dict[str, Any]:
        """
        Analyze the sentiment of the provided text.
        
        Args:
            text: The text to analyze
            
        Returns:
            Dict containing sentiment analysis results
        """
        if not text or not text.strip():
            raise ValueError("Text cannot be empty")
        
        try:
            # Use TextBlob for sentiment analysis
            analysis = TextBlob(text)
            
            # Get polarity and subjectivity
            polarity = analysis.sentiment.polarity
            subjectivity = analysis.sentiment.subjectivity
            
            # Determine sentiment category
            if polarity > 0.1:
                sentiment = "positive"
            elif polarity < -0.1:
                sentiment = "negative"
            else:
                sentiment = "neutral"
            
            logger.debug(f"Analyzed text with polarity {polarity} and subjectivity {subjectivity}")
            
            return {
                "text": text,
                "sentiment": sentiment,
                "polarity": polarity,
                "subjectivity": subjectivity
            }
        except Exception as e:
            logger.error(f"Error analyzing text sentiment: {e}")
            raise


# Create a singleton instance of the service
sentiment_service = SentimentAnalysisService()
