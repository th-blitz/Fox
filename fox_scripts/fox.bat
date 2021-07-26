@echo off
set arg1=%1
set arg2=%2
set arg3=%3

set foxpath=%~dp0

set foxpath=%foxpath:\fox_scripts\=%

set bridge=\bridge.py
set py_exe=\fox_py\python.exe

set bridge=%foxpath%%bridge%
set fox_py=%foxpath%%py_exe%

%fox_py% %bridge% %arg1% %arg2% %arg3%

if not defined arg1 set arg1=_no_

if %arg1%==activate (
fox_%arg2%
)

if %arg1%==deactivate (
deactivate
)
