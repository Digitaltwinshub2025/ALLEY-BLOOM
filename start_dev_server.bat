@echo off
cd /d "%~dp0"
set FLASK_ENV=development
set FLASK_DEBUG=1
python app.py
pause
