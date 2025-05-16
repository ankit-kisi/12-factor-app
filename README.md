# Text Sentiment Analysis API

A FastAPI application for analyzing text sentiment and emotions.

## Quick Setup

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/ankit-kisi/12-factor-app.git
cd 12-factor-app

# 2. Create and activate virtual environment
python3.11 -m venv venv_py311
source venv_py311/bin/activate  # On Windows: venv_py311\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt
```

### Running the API

```bash
# Start the server
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

The API will be available at:

- http://localhost:8000
- Swagger UI: http://localhost:8000/api/v1/docs

## Using the API

### API Endpoints

#### 1. Sentiment Analysis

**Endpoint**: `POST /api/v1/sentiment/sentiment`

**Example with curl:**

```bash
curl -X 'POST' 'http://localhost:8000/api/v1/sentiment/sentiment' \
  -H 'Content-Type: application/json' \
  -d '{"text": "I absolutely love this product. It is amazing!"}'
```

**Example response:**

```json
{
  "text": "I absolutely love this product. It is amazing!",
  "sentiment": "positive",
  "polarity": 0.625,
  "subjectivity": 0.75
}
```

#### 2. Health Check

**Endpoint**: `GET /api/v1/sentiment/health`

**Example with curl:**

```bash
curl -X 'GET' 'http://localhost:8000/api/v1/sentiment/health'
```

## Understanding Results

- **sentiment**: The overall emotion (positive, negative, or neutral)
- **polarity**: The sentiment strength (-1.0 to 1.0, where -1 is very negative and 1 is very positive)
- **subjectivity**: How subjective/opinionated the text is (0.0 to 1.0, where 0 is objective and 1 is subjective)

## Troubleshooting

If you encounter "Address already in use" errors:

```bash
pkill -f uvicorn
```
