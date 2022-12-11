"""
Usage:
    python winsetup.py py2exe
"""
from distutils.core import setup
import py2exe

APP = ['index.py']
DATA_FILES = ['icon.jpeg']
OPTIONS = {
    "iconfile": "icon.jpeg"
}

setup(
    windows=APP,
    data_files=DATA_FILES,
    options={'py2exe': OPTIONS},
    setup_requires=['py2exe'],
    name="Discord Mafia Advertising"
)
