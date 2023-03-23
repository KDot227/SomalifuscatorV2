@echo off
::pemdas shi
set /a test=10 + 10 / 2

if %test%==10 (
    echo %t% is 10
) else (
    echo ans is not 10
    echo ans is %test%
)

pause
exit