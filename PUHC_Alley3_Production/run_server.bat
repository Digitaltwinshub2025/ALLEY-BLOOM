@echo off
setlocal

REM Run from this folder
pushd "%~dp0"

REM Create virtual environment if missing
if not exist ".venv\Scripts\python.exe" (
  echo Creating virtual environment in .venv...
  python -m venv .venv
  if errorlevel 1 (
    echo Failed to create virtual environment.
    popd
    exit /b 1
  )
)

REM Activate venv
call ".venv\Scripts\activate.bat"
if errorlevel 1 (
  echo Failed to activate virtual environment.
  popd
  exit /b 1
)

REM Install dependencies
echo Installing dependencies...
python -m pip install --upgrade pip setuptools wheel
python -m pip install --no-cache-dir -r requirements.txt
if errorlevel 1 (
  echo Failed to install dependencies.
  echo If you see a WinError 32 file-in-use error, close any running Python processes and delete the .venv folder, then re-run this script.
  popd
  exit /b 1
)

REM Run server
set FLASK_ENV=development
echo Starting server on http://localhost:5000 ...
python app.py

popd
endlocal
