# Unreal Pixel Streaming Connection Checker

Write-Host "================================" -ForegroundColor Cyan
Write-Host "Pixel Streaming Connection Check" -ForegroundColor Cyan
Write-Host "================================" -ForegroundColor Cyan
Write-Host ""

# Check Signaling Server (Port 80)
Write-Host "1. Checking Signaling Server (Port 80)..." -ForegroundColor Yellow
$port80 = Test-NetConnection -ComputerName localhost -Port 80 -WarningAction SilentlyContinue
if ($port80.TcpTestSucceeded) {
    Write-Host "   ✓ Port 80 is OPEN (Signaling Server HTTP)" -ForegroundColor Green
} else {
    Write-Host "   ✗ Port 80 is CLOSED" -ForegroundColor Red
}

# Check WebSocket Port (8888)
Write-Host "2. Checking WebSocket Port (8888)..." -ForegroundColor Yellow
$port8888 = Test-NetConnection -ComputerName localhost -Port 8888 -WarningAction SilentlyContinue
if ($port8888.TcpTestSucceeded) {
    Write-Host "   ✓ Port 8888 is OPEN (Unreal Streamer Connection)" -ForegroundColor Green
} else {
    Write-Host "   ✗ Port 8888 is CLOSED" -ForegroundColor Red
}

# Check Flask App (Port 5000)
Write-Host "3. Checking Flask App (Port 5000)..." -ForegroundColor Yellow
$port5000 = Test-NetConnection -ComputerName localhost -Port 5000 -WarningAction SilentlyContinue
if ($port5000.TcpTestSucceeded) {
    Write-Host "   ✓ Port 5000 is OPEN (Flask Web App)" -ForegroundColor Green
} else {
    Write-Host "   ✗ Port 5000 is CLOSED" -ForegroundColor Red
}

Write-Host ""
Write-Host "================================" -ForegroundColor Cyan
Write-Host "Status Summary" -ForegroundColor Cyan
Write-Host "================================" -ForegroundColor Cyan

if ($port80.TcpTestSucceeded -and $port8888.TcpTestSucceeded -and $port5000.TcpTestSucceeded) {
    Write-Host "✓ All servers are running!" -ForegroundColor Green
    Write-Host ""
    Write-Host "Next Steps:" -ForegroundColor Yellow
    Write-Host "1. Check if Unreal Engine is running" -ForegroundColor White
    Write-Host "2. Open: http://localhost:5000/unreal-viewer" -ForegroundColor White
    Write-Host "3. Look for 'Streamer connected' in signaling server logs" -ForegroundColor White
} else {
    Write-Host "✗ Some servers are not running" -ForegroundColor Red
    Write-Host ""
    Write-Host "Troubleshooting:" -ForegroundColor Yellow
    if (-not $port80.TcpTestSucceeded) {
        Write-Host "- Restart signaling server: .\start.bat" -ForegroundColor White
    }
    if (-not $port5000.TcpTestSucceeded) {
        Write-Host "- Restart Flask app: py app.py" -ForegroundColor White
    }
}

Write-Host ""
Write-Host "================================" -ForegroundColor Cyan
Write-Host "Quick Links" -ForegroundColor Cyan
Write-Host "================================" -ForegroundColor Cyan
Write-Host "Signaling Server: http://localhost:80" -ForegroundColor White
Write-Host "Flask Web App:    http://localhost:5000" -ForegroundColor White
Write-Host "Unreal Viewer:    http://localhost:5000/unreal-viewer" -ForegroundColor White
Write-Host ""

# Check for Unreal process
Write-Host "================================" -ForegroundColor Cyan
Write-Host "Checking for Unreal Process" -ForegroundColor Cyan
Write-Host "================================" -ForegroundColor Cyan

$unrealProcess = Get-Process -Name "UnrealEditor*" -ErrorAction SilentlyContinue
if ($unrealProcess) {
    Write-Host "✓ Unreal Editor is RUNNING" -ForegroundColor Green
    Write-Host "   Process: $($unrealProcess.ProcessName)" -ForegroundColor White
    Write-Host "   PID: $($unrealProcess.Id)" -ForegroundColor White
} else {
    Write-Host "X Unreal Editor is NOT RUNNING" -ForegroundColor Red
    Write-Host ""
    Write-Host "To launch Unreal with Pixel Streaming:" -ForegroundColor Yellow
    Write-Host "UnrealEditor.exe PROJECT.uproject -game -PixelStreamingURL=ws://localhost:8888" -ForegroundColor Cyan
}

Write-Host ""
