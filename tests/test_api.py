"""Tests for the API endpoints."""
from fastapi.testclient import TestClient
import pytest
from app.main import app


client = TestClient(app)


class TestSentimentEndpoints:
    """Test cases for sentiment analysis endpoints."""
    
    def test_analyze_sentiment_endpoint(self):
        """Test the sentiment analysis endpoint with valid input."""
        response = client.post(
            "/api/v1/sentiment/sentiment",
            json={"text": "I love this product, it's amazing!"}
        )
        assert response.status_code == 200
        data = response.json()
        assert data["text"] == "I love this product, it's amazing!"
        assert data["sentiment"] == "positive"
        assert data["polarity"] > 0
        assert 0 <= data["subjectivity"] <= 1
    
    def test_analyze_sentiment_with_empty_text(self):
        """Test the sentiment analysis endpoint with empty text."""
        response = client.post(
            "/api/v1/sentiment/sentiment",
            json={"text": ""}
        )
        assert response.status_code == 400
        assert "detail" in response.json()
    
    def test_health_check_endpoint(self):
        """Test the health check endpoint."""
        response = client.get("/api/v1/sentiment/health")
        assert response.status_code == 200
        assert response.json() == {"status": "healthy"}
