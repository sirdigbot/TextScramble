@echo off
python -O -m PyInstaller --noconfirm --noconsole --noupx --onefile --clean --icon="textscramble.ico" --name TextScramble --distpath ./bin --workpath ./build scramble.pyw
