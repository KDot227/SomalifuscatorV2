@echo off
cd /d "%~dp0"

color 0a
title SomalifuscatorV2
cls

set "python_path=%localappdata%\Programs\Python"

if not exist "%python_path%" (
    echo "would you like to install python? (y/n)"
    set /p "install_python="
    if "%install_python%" == "y" (
        :: lowkey stole this from addix but I made my own and cant find it
        for /f "tokens=1,2 delims= " %%a in ('powershell -Command "Invoke-WebRequest https://www.python.org/ftp/python/ -UseBasicParsing | Select-String -Pattern '3.11.[0-9]{1,2}' -AllMatches | Select-Object -ExpandProperty Matches | Select-Object -ExpandProperty Value | Sort-Object -Descending -Unique | Select-Object -First 1"') do (
            set "PYTHON_VERSION=%%a%%b"
        )
        set "PYTHON_URL=https://www.python.org/ftp/python/%PYTHON_VERSION%/python-%PYTHON_VERSION%-amd64.exe"
        set "PYTHON_EXE=python-installer.exe"

        curl -L -o %PYTHON_EXE% %PYTHON_URL%

        start /wait %PYTHON_EXE% /quiet /passive InstallAllUsers=0 PrependPath=1 Include_test=0 Include_pip=1 Include_doc=0

        del %PYTHON_EXE%
    ) else (
        echo please install python and add it to path
        pause
        exit /b 1
    )
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

if "%~1"=="" (
    pushd src
    python -m main
    popd
    pause
) else (
    pushd src
    python -m main -f %~1
    popd
)

exit /b 0