@echo off

echo %~dp0 %~dp0

set "test=test"

if "%test%" == "test" (
    echo test 1
    echo test 2
)

if "test" == "test" (
    echo test 3
)
if "test" == "test" (
    echo test 4
    echo test 5
)
if "test" == "test" (
    echo test 6
)