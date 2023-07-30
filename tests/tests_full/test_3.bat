@echo off
setlocal
echo this is a test && echo %~dp0
goto :test
echo didn't work
pause
exit

:test
echo worked
exit /b 0