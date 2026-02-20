@echo off
echo ============================================================
echo  Alley Bloom - GitHub Deployment Helper
echo ============================================================
echo.

REM Check if git is initialized
if not exist .git (
    echo Initializing Git repository...
    git init
    echo.
)

echo Adding all files to Git...
git add .
echo.

echo Enter commit message (or press Enter for default):
set /p commit_msg="Commit message: "
if "%commit_msg%"=="" set commit_msg=Update Alley Bloom platform

echo.
echo Committing changes...
git commit -m "%commit_msg%"
echo.

echo ============================================================
echo  NEXT STEPS:
echo ============================================================
echo.
echo 1. Create a GitHub repository at: https://github.com/new
echo    - Name it: alley-bloom
echo    - Make it Public or Private
echo    - Don't initialize with README
echo.
echo 2. Copy your GitHub username and run this command:
echo    git remote add origin https://github.com/YOUR_USERNAME/alley-bloom.git
echo.
echo 3. Push to GitHub:
echo    git branch -M main
echo    git push -u origin main
echo.
echo 4. Deploy to Render:
echo    - Go to https://render.com
echo    - Sign up with GitHub
echo    - Create New Web Service
echo    - Connect your alley-bloom repository
echo    - Choose Free plan
echo    - Deploy!
echo.
echo ============================================================
echo  See DEPLOYMENT_INSTRUCTIONS.md for detailed steps
echo ============================================================
echo.
pause
