@echo off

pause

echo test > test.txt
type test.txt
echo test >> test.txt
type test.txt

del test.txt
timeout 3
exit /b 0