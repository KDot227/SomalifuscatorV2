@echo off

::https://stackoverflow.com/questions/4051883/batch-script-how-to-check-for-admin-rights

echo Administrative permissions required. Detecting permissions...
net session >nul 2>&1
if %errorLevel% == 0 (
    echo Success: Administrative permissions confirmed.
) else (
    echo Failure: Current permissions inadequate.
)
exit /b 0