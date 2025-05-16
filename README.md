# Text Sentiment Analysis API

A FastAPI application for analyzing text sentiment following 12-factor app principles.

## Features

- Analyze text sentiment (positive, negative, or neutral)
- Get polarity and subjectivity scores for text
- RESTful API with SwaggerUI documentation

## Requirements

- Python 3.7 - 3.12 (Python 3.13 has compatibility issues with some dependencies)
- Dependencies listed in `requirements.txt`

## Installation

1. Clone the repository:

```bash
git clone <repository-url>
cd 12-factor-calc
```

2. Create a virtual environment and activate it:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

## Configuration

This application follows the 12-factor app principles. Configuration is handled through environment variables in the `.env` file.

Key environment variables:

- `APP_NAME`: Name of the application (default: sentiment-analysis-api)
- `ENV`: Current environment (development, testing, production)
- `DEBUG`: Debug mode (True/False)
- `LOG_LEVEL`: Logging level (debug, info, warning, error)
- `API_V1_STR`: API version prefix
- `ALLOWED_ORIGINS`: CORS allowed origins

## Running the Application

### Option 1: Using Docker (Recommended)

This method works regardless of your Python version:

```bash
# Build and start the Docker container
docker-compose up

# Or to run in the background
docker-compose up -d
```

### Option 2: Running locally

If you have a compatible Python version (3.7-3.12):

```bash
# Make the script executable if not already
chmod +x start.sh

# Run the application
./start.sh
```

Or run manually:

```bash
uvicorn app.main:app --reload
```

Or use the main.py script:

```bash
python -m app.main
```

The API will be available at http://localhost:8000

API documentation is available at:

- Swagger UI: http://localhost:8000/api/v1/docs
- ReDoc: http://localhost:8000/api/v1/redoc

## Testing

To run tests:

```bash
pytest
```

## API Endpoints

### Sentiment Analysis

```
POST /api/v1/sentiment/sentiment
```

Request body:

```json
{
  "text": "This is a sample text for sentiment analysis"
}
```

Response:

```json
{
  "text": "This is a sample text for sentiment analysis",
  "sentiment": "neutral",
  "polarity": 0.0,
  "subjectivity": 0.0
}
```

### Health Check

```
GET /api/v1/sentiment/health
```

Response:

```json
{
  "status": "healthy"
}
```

## Troubleshooting

### Python 3.13 Compatibility Issues

If you're using Python 3.13, you might encounter compatibility issues with some dependencies, especially with FastAPI and Pydantic. The following error might occur:

```
TypeError: ForwardRef._evaluate() missing 1 required keyword-only argument: 'recursive_guard'
```

Solution:

- Use Python 3.7 - 3.12 instead
- If you must use Python 3.13, consider installing the dependencies with the `--no-deps` flag and manually installing compatible versions of the transitive dependencies.

### NLTK Data Download Issues

If you encounter errors related to NLTK data, you can manually download it:

```python
import nltk
nltk.download('punkt')
```

## 12-Factor App Principles

This application follows the 12-factor app methodology:

1. **Codebase**: Single codebase tracked in version control
2. **Dependencies**: Explicitly declared and isolated dependencies
3. **Config**: Configuration stored in environment variables
4. **Backing Services**: Backing services treated as attached resources (not applicable)
5. **Build, release, run**: Strict separation of build and run stages
6. **Processes**: Stateless processes
7. **Port binding**: Services exported via port binding
8. **Concurrency**: Scale via process model
9. **Disposability**: Fast startup and graceful shutdown
10. **Dev/prod parity**: Development, staging, and production as similar as possible
11. **Logs**: Logs treated as event streams
12. **Admin processes**: Admin/maintenance tasks as one-off processes (not applicable)
