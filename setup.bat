@echo off
cd /d "%~dp0"

color 0a
title SomalifuscatorV2
cls

set "python_path=%localappdata%\Programs\Python"

echo %python_path%

if not exist "%python_path%" (
    echo "Python may not be installed. fr fr."
    pause
)

python --version
if not %errorlevel% == 0 (
    echo Python is most likely installed but NOT added to path. Please follow this video to fix
    timeout /t 3 /nobreak
    start https://www.youtube.com/watch?v=4bUOrMj88Pc&ab_channel=LearningLad
    pause
    exit /b 1
)

python -m pip install -r requirements.txt --upgrade

pushd src
python -m main
popd

if %USERNAME%==this1 (
    pyclean .
)

exit /b 0