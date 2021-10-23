@echo off
py -OO -m PyInstaller main.py -p modules -n "LCLPy" --workpath "%TEMP%" --specpath %TEMP% --noconfirm --onefile --icon NONE
pause
