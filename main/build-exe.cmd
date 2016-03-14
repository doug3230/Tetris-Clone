pyinstaller --onefile --noconsole Tetris-Clone.py
rmdir build /s /q
del Tetris-Clone.spec
del Tetris-Clone.exe
move dist\Tetris-Clone.exe .
rmdir dist /s /q