@echo off
SETLOCAL EnableDelayedExpansion

set first=first
set "second=second"

set "_var=first"
set "_var=second" & Echo %_var% !_var!

set third=third
set "fourth=fourth"

echo %first% %second% %third% %fourth%
echo %first% %second% %third% %fourth%
echo %first% %second% %third% %fourth%

pause
exit