@echo off
echo ========================================
echo   Launching Unreal with Pixel Streaming
echo ========================================
echo.
echo Starting Unreal Engine in Game Mode...
echo This will take 1-2 minutes to load.
echo.
echo Look for the Unreal game window to appear.
echo When ready, it will connect to the signaling server.
echo.

"D:\Epic Games\UE_5.6\Engine\Binaries\Win64\UnrealEditor.exe" "D:\PUHC_Unreal_Test\PUHC_Unreal_Test.uproject" -game -PixelStreamingURL=ws://localhost:8888 -RenderOffScreen -AudioMixer

pause
