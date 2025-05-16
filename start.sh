#!/bin/bash
# Start the FastAPI application

# Ensure we're in the right directory
cd "$(dirname "$0")"

# Activate the virtual environment if it exists
if [ -d "venv" ]; then
    echo "Activating virtual environment..."
    source venv/bin/activate
fi

# Check if dependencies are installed
if ! pip show fastapi > /dev/null 2>&1; then
    echo "Installing dependencies..."
    pip install -r requirements.txt
fi

# Download NLTK data if needed
python -c "import nltk; nltk.download('punkt', quiet=True)"

# Run the application
echo "Starting Sentiment Analysis API..."
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

# Deactivate the virtual environment
if [ -d "venv" ]; then
    deactivate 2> /dev/null
fi
