@echo off
echo ========================================
echo   Starting Alley Bloom with Pixel Streaming
echo ========================================
echo.

echo [1/3] Starting Signaling Server...
start "Signaling Server" cmd /k "cd /d D:\Epic Games\UE_5.6\Engine\Plugins\Media\PixelStreaming2\Resources\WebServers\SignallingWebServer\platform_scripts\cmd && start.bat"
timeout /t 5 /nobreak

echo [2/3] Starting Unreal Engine with Pixel Streaming...
start "Unreal Engine" "D:\Epic Games\UE_5.6\Engine\Binaries\Win64\UnrealEditor.exe" "D:\PUHC_Unreal_Test\PUHC_Unreal_Test.uproject" -game -PixelStreamingURL=ws://localhost:8888 -RenderOffScreen -AudioMixer
timeout /t 10 /nobreak

echo [3/3] Starting Flask Website...
start "Flask Website" cmd /k "cd /d c:\Users\MLee7\Desktop\101225windsurf\CascadeProjects\splitwise && py app.py"
timeout /t 3 /nobreak

echo.
echo ========================================
echo   All Services Started!
echo ========================================
echo.
echo Flask Website: http://localhost:5000
echo Network Access: http://10.118.83.126:5000
echo Unreal Viewer: http://localhost:5000/unreal-viewer
echo.
echo Press any key to exit (services will keep running)...
pause
