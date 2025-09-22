@echo off
echo Starting Flask Application...
echo.
echo Make sure to:
echo 1. Open your web browser
echo 2. Go to: http://127.0.0.1:5000
echo 3. Do NOT open HTML files directly!
echo.
echo Press Ctrl+C to stop the server
echo.
cd /d "%~dp0"
python BTPW_FlaskWeb.py
pause
