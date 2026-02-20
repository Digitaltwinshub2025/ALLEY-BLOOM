@echo off
echo.
echo ========================================
echo   Starting Alley Bloom Server
echo ========================================
echo.

REM Get local IP address
for /f "tokens=2 delims=:" %%a in ('ipconfig ^| findstr /c:"IPv4 Address"') do (
    set IP=%%a
    goto :found
)
:found
set IP=%IP:~1%

echo Local Access:    http://localhost:5000
echo Network Access:  http://%IP%:5000
echo.
echo Share the Network URL with workshop participants!
echo Press Ctrl+C to stop the server
echo.
echo ========================================
echo.

REM Start Flask app using py launcher
py app.py

pause
