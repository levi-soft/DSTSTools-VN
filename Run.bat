@echo off
:: Create virtual environment
python -m venv dststool_env

:: Activate virtual environment
call dststool_env\Scripts\activate

:: Install dependencies in virtual environment
pip install PyQt6

:: Run application
python DSTSToolGUIV2.py

