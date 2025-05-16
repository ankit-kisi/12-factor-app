"""Middleware configuration for the application."""
import time
import logging
from fastapi import Request
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.base import BaseHTTPMiddleware
from app.core.config import settings

# Create logger
logger = logging.getLogger(__name__)


class LoggingMiddleware(BaseHTTPMiddleware):
    """Middleware for logging requests and responses."""
    
    async def dispatch(self, request: Request, call_next):
        """Process the request and log details."""
        start_time = time.time()
        
        # Get request details
        path = request.url.path
        method = request.method
        
        # Log the request
        logger.info(f"Request: {method} {path}")
        
        # Process the request
        response = await call_next(request)
        
        # Calculate processing time
        process_time = time.time() - start_time
        
        # Log the response
        logger.info(
            f"Response: {method} {path} - Status: {response.status_code} - Time: {process_time:.3f}s"
        )
        
        return response


def setup_middleware(app):
    """Configure all middleware."""
    # Set up CORS
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.ALLOWED_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    
    # Set up request logging
    app.add_middleware(LoggingMiddleware)
