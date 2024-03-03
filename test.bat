echo off
SETLOCAL EnableDelayedExpansion
for /F "tokens=1,2 delims=#" %%a in ('"prompt #$H#$E# & echo on & for %%b in (1) do rem"') do (
  set "DEL=%%a"
)
echo say the name of the colors, don't read

call :ColorText 0a "blue"
call :ColorText 0C "green"
call :ColorText 0b "red"
echo(
call :ColorText 19 "yellow"
call :ColorText 2F "black"
call :ColorText 4e "white"

goto :eof

:ColorText
echo off
<nul set /p ".=%DEL%" > "%~2"
findstr /v /a:%1 /R "^$" "%~2" nul
del "%~2" > nul 2>&1
goto :eof