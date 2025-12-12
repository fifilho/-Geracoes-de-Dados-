@echo off
echo  ================== GERANDO O EXE ATUALIZADO ==================

python -m PyInstaller --onefile launcher.py >nul 2>&1

echo  ================== Arquivo em: dist\launcher.exe ==================

:: Eu N sei usar Bar mas o Chat gpt Sabe::
pause