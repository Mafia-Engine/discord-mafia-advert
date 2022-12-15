python -m pip install --upgrade pip
python -m pip install --upgrade Pillow
python -m pip install pyinstaller

python -m PyInstaller --noconfirm --onefile --windowed --hidden-import="PIL" --icon "icon.jpeg" --add-data "icon.jpeg;." --name "Discord Mafia Advertising"  "index.py"