@echo off
cython scramble.pyw --embed -3
echo C File Generated with Cython Successfully. You will need to compile it separately.
echo =================
echo PLEASE NOTE:
echo You will need to manually edit the generated C file and change
echo    "int wmain(.."
echo into
echo    "int main(.."
echo This is because you cannot use /subsystem:windows /ENTRY:mainCRTStartup
echo if the main function is not actually called "main".
echo =================
pause
