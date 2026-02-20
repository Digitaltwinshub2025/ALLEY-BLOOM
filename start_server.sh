#!/bin/bash
# Bash script to start the production server
# For Linux/Mac deployment

echo "🌸 Starting Alley Bloom Production Server..."

# Check if virtual environment exists
if [ -d "venv" ]; then
    echo "✓ Activating virtual environment..."
    source venv/bin/activate
else
    echo "⚠ No virtual environment found. Creating one..."
    python3 -m venv venv
    source venv/bin/activate
    echo "✓ Installing dependencies..."
    pip install -r requirements.txt
    pip install gunicorn eventlet
fi

# Get local IP address
LOCAL_IP=$(hostname -I | awk '{print $1}')

echo ""
echo "========================================"
echo "🌸 Alley Bloom Server Starting"
echo "========================================"
echo ""
echo "Local Access:    http://localhost:5000"
echo "Network Access:  http://${LOCAL_IP}:5000"
echo ""
echo "Share the Network URL with other residents!"
echo "Press Ctrl+C to stop the server"
echo ""

# Start the server
python app.py
