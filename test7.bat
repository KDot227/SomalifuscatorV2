@echo off

goto :start2

:start1
goto :start3

:start2
goto :start1

:start3
echo worked!
pause