@echo off
cd /d "%~dp0"

:: Initialize script
call :initialize

:: Check Python installation
call :check_python_installation

:: Check if Python is in PATH
call :check_python_path

:: Upgrade requirements
call :install_requirements

:: Run main script
call :run_main_script "%~1"

:: End script
exit /b 0

:initialize
    color 0a
    title SomalifuscatorV2
    cls
    set "python_path=%localappdata%\Programs\Python"
    set "requirements_file=requirements.txt"
goto :eof

:check_python_installation
    if not exist "%python_path%" (
        echo "Would you like to install Python? (y/n)"
        set /p "install_python="
        if "%install_python%" == "y" (
            call :install_python
        ) else (
            echo Please install Python and add it to the PATH.
            pause
            exit /b 1
        )
    )
goto :eof

:install_python
    :: Check if curl and PowerShell are available
    curl --version >nul 2>&1 || (
        echo curl is required but not installed.
        pause
        exit /b 1
    )
    powershell -Command "echo 'test'" >nul 2>&1 || (
        echo PowerShell is required but not available.
        pause
        exit /b 1
    )
    
    :: Get the latest Python version
    for /f "tokens=1,2 delims= " %%a in ('powershell -Command "Invoke-WebRequest https://www.python.org/ftp/python/ -UseBasicParsing | Select-String -Pattern '3.11.[0-9]{1,2}' -AllMatches | Select-Object -ExpandProperty Matches | Select-Object -ExpandProperty Value | Sort-Object -Descending -Unique | Select-Object -First 1"') do (
        set "PYTHON_VERSION=%%a%%b"
    )
    
    :: Download and install Python
    set "PYTHON_URL=https://www.python.org/ftp/python/%PYTHON_VERSION%/python-%PYTHON_VERSION%-amd64.exe"
    set "PYTHON_EXE=python-installer.exe"
    curl -L -o %PYTHON_EXE% %PYTHON_URL%
    start /wait %PYTHON_EXE% /quiet /passive InstallAllUsers=0 PrependPath=1 Include_test=0 Include_pip=1 Include_doc=0
    del %PYTHON_EXE%
goto :eof

:check_python_path
    python --version >nul 2>&1
    if not %errorlevel% == 0 (
        echo Python is either not installed or not added to the PATH. Please follow this video to fix:
        timeout /t 3 /nobreak
        start https://www.youtube.com/watch?v=4bUOrMj88Pc&ab_channel=LearningLad
        pause
        exit /b 1
    )
goto :eof

:install_requirements
    if exist "%requirements_file%" (
        python -m pip install -r %requirements_file% --upgrade
    ) else (
        echo "%requirements_file%" does not exist. Skipping package upgrade.
    )
goto :eof

:run_main_script
    pushd src
    if "%~1"=="" (
        python -m main
    ) else (
        python -m main -f %~1
    )
    popd
goto :eof
