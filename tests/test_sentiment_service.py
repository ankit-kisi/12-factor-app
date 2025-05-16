"""Tests for the sentiment analysis service."""
import pytest
from app.services.sentiment import SentimentAnalysisService


class TestSentimentAnalysisService:
    """Test cases for the SentimentAnalysisService."""
    
    def setup_method(self):
        """Set up the test case."""
        self.service = SentimentAnalysisService()
    
    def test_analyze_positive_text(self):
        """Test analyzing text with positive sentiment."""
        result = self.service.analyze_text("I love this product, it's amazing!")
        assert result["sentiment"] == "positive"
        assert result["polarity"] > 0
        assert 0 <= result["subjectivity"] <= 1
    
    def test_analyze_negative_text(self):
        """Test analyzing text with negative sentiment."""
        result = self.service.analyze_text("I hate this product, it's terrible.")
        assert result["sentiment"] == "negative"
        assert result["polarity"] < 0
        assert 0 <= result["subjectivity"] <= 1
    
    def test_analyze_neutral_text(self):
        """Test analyzing text with neutral sentiment."""
        result = self.service.analyze_text("This is a fact about the product.")
        # Neutral could be slightly positive or negative depending on the analysis
        assert -0.1 <= result["polarity"] <= 0.1
        assert 0 <= result["subjectivity"] <= 1
    
    def test_empty_text(self):
        """Test analyzing empty text."""
        with pytest.raises(ValueError):
            self.service.analyze_text("")
