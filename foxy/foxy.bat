@echo off

set arg1=%1

if not defined arg1 (
set arg1=python38
)

set exiting=_no_

if defined arg1 set pyversion=%arg1%
if %arg1%==exit set exiting=exit


if %exiting%==_no_ (
echo -
echo - selected folder %pyversion% 
echo - foxy py_folder_name
echo - foxy exit
)

set foxpath=%~dp0

set foxpath=%foxpath:\foxy\=%

set foxscripts=\fox_scripts

set foxscripts=%foxpath%%foxscripts%

set foxscriptspy=%foxscripts%\%arg1%

set pythondefault=\python\%pyversion%
set pythondefault=%foxpath%%pythondefault%

set pythonscripts=\python\%pyversion%\Scripts
set pythonscripts=%foxpath%%pythonscripts%

if not defined oldpath set "oldpath=%PATH%"

set "PATH=%oldpath%"

set "PATH=%foxscripts%;%PATH%"
set "PATH=%pythondefault%;%PATH%"
set "PATH=%pythonscripts%;%PATH%"
set "PATH=%foxscriptspy%;%PATH%"

set farg=(F_%arg1%)

if not defined oldprompt set oldprompt=%PROMPT%
if not defined oldfarg set oldfarg=%farg%

set PROMPT=%oldprompt%

set PROMPT=%farg% %PROMPT%

set oldfarg=%farg%


if %exiting%==exit (
set "PATH=%oldpath%"
set PROMPT=%oldprompt%
set fprompt=
set farg=
set oldfarg=
)
