pyinstaller -p "core/constants" -p "core/customization" -p "core/elements" -p "core/game" -p "core-tetris-clone/tcustomization" -p "core-tetris-clone/telements" -p "core-tetris-clone/tgame" --onefile --debug main/Tetris-Clone.py
rmdir build /s /q
del Tetris-Clone.spec
set wd=%cd%
set filesd="%wd%\main\files"
mkdir "C:\Users\Richard\Documents\GitHub\Tetris-Clone\Tetris-Clone\files"
cd "C:\Users\Richard\Documents\GitHub\Tetris-Clone\Tetris-Clone\files"
xcopy %filesd% /s /e
cd %wd%