# Alley Bloom - Easy Development Server Starter
# This script starts the Flask server with auto-reload enabled

Write-Host "🎨 Starting Alley Bloom Development Server..." -ForegroundColor Cyan
Write-Host ""
Write-Host "📝 Quick Tips:" -ForegroundColor Yellow
Write-Host "  • Server will auto-reload when you save files" -ForegroundColor Gray
Write-Host "  • Press Ctrl+C to stop the server" -ForegroundColor Gray
Write-Host "  • Edit files in templates/ and static/ folders" -ForegroundColor Gray
Write-Host ""
Write-Host "🌐 Access your site at:" -ForegroundColor Green
Write-Host "  → http://localhost:5000" -ForegroundColor White
Write-Host ""
Write-Host "📁 Main pages:" -ForegroundColor Green
Write-Host "  → http://localhost:5000              (Landing page)" -ForegroundColor White
Write-Host "  → http://localhost:5000/street-view-designer  (Street Explorer)" -ForegroundColor White
Write-Host "  → http://localhost:5000/neighborhoods         (Neighborhood selector)" -ForegroundColor White
Write-Host ""
Write-Host "Starting server now..." -ForegroundColor Cyan
Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor DarkGray
Write-Host ""

# Set environment variable for Flask development mode
$env:FLASK_ENV = "development"

# Start the Flask app
python app.py
