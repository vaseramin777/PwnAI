@ECHO OFF    // Prevents the command prompt from displaying the commands

pushd %~dp0  // Changes the current directory to the directory where this script is located

REM Command file for Sphinx documentation

if "%SPHINXBUILD%" == "" (   // Checks if the SPHINXBUILD environment variable is set
	set SPHINXBUILD=sphinx-build   // If not, sets the SPHINXBUILD variable to the 'sphinx-build' executable path
)
set SOURCEDIR=source  // Sets the SOURCEDIR variable to the source directory for the Sphinx documentation
set BUILDDIR=build    // Sets the BUILDDIR variable to the build directory for the Sphinx documentation

%SPHINXBUILD% >NUL 2>NUL   // Calls the 'sphinx-build' command and redirects the output to null
if errorlevel 9009 (         // Checks if the 'sphinx-build' command failed
	echo.                   // Displays an error message if the command failed
	echo.The 'sphinx-build' command was not found. Make sure you have Sphinx
	echo.installed, then set the SPHINXBUILD environment variable to point
	echo.to the full path of the 'sphinx-build' executable. Alternatively you
	echo.may add the Sphinx directory to PATH.
	echo.
	echo.If you don't have Sphinx installed, grab it from
	echo.https://www.sphinx-doc.org/
	exit /b 1
)

if "%1" == "" goto help   // Checks if a command was provided as an argument

%SPHINXBUILD% -M %1 %SOURCEDIR% %BUILDDIR% %SPHINXOPTS% %O%   // Calls the 'sphinx-build' command with the provided argument
goto end

:help   // Displays the help message
%SPHINXBUILD% -M help %SO
