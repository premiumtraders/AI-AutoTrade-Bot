@echo off
setlocal enabledelayedexpansion

REM Check if Python is installed
python --version 2>nul
if %errorlevel% neq 0 (
    echo Python is not installed. Downloading and installing Python...

    REM Download and install Python
    bitsadmin.exe /transfer PythonInstaller https://www.python.org/ftp/python/3.12.1/python-3.12.1-amd64.exe %temp%\python_installer.exe
    %temp%\python_installer.exe /quiet InstallAllUsers=1 PrependPath=1

    REM Check again after installation
    python --version 2>nul
    if %errorlevel% neq 0 (
        echo An error occurred while installing Python. Please install it manually.
        exit /b 1
    ) else (
        echo Python has been successfully installed.
    )
) else (
    echo Python is already installed.
)

REM Run the Python script
python3 main.py
