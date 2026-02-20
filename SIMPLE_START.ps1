# Simple PowerShell script to start Alley Bloom
# Uses 'py' launcher which is already installed on your system

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  Starting Alley Bloom Server" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Get local IP
$localIP = (Get-NetIPAddress -AddressFamily IPv4 | Where-Object {$_.InterfaceAlias -notlike "*Loopback*" -and $_.IPAddress -notlike "169.254.*"} | Select-Object -First 1).IPAddress

Write-Host "Local Access:    http://localhost:5000" -ForegroundColor White
Write-Host "Network Access:  http://${localIP}:5000" -ForegroundColor Yellow
Write-Host ""
Write-Host "Share the Network URL with workshop participants!" -ForegroundColor Green
Write-Host "Press Ctrl+C to stop the server" -ForegroundColor Gray
Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Start Flask app using py launcher
py app.py
