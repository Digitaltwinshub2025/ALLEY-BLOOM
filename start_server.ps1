# PowerShell script to start the production server
# For Windows deployment

Write-Host "🌸 Starting Alley Bloom Production Server..." -ForegroundColor Cyan

# Check if virtual environment exists
if (Test-Path "venv") {
    Write-Host "✓ Activating virtual environment..." -ForegroundColor Green
    .\venv\Scripts\Activate.ps1
} else {
    Write-Host "⚠ No virtual environment found. Creating one..." -ForegroundColor Yellow
    python -m venv venv
    .\venv\Scripts\Activate.ps1
    Write-Host "✓ Installing dependencies..." -ForegroundColor Green
    pip install -r requirements.txt
    pip install gunicorn eventlet
}

# Get local IP address
$localIP = (Get-NetIPAddress -AddressFamily IPv4 | Where-Object {$_.InterfaceAlias -notlike "*Loopback*" -and $_.IPAddress -notlike "169.254.*"} | Select-Object -First 1).IPAddress

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "🌸 Alley Bloom Server Starting" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Local Access:    http://localhost:5000" -ForegroundColor White
Write-Host "Network Access:  http://${localIP}:5000" -ForegroundColor Yellow
Write-Host ""
Write-Host "Share the Network URL with other residents!" -ForegroundColor Green
Write-Host "Press Ctrl+C to stop the server" -ForegroundColor Gray
Write-Host ""

# Start the server
python app.py
