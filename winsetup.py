"""
Usage:
    python winsetup.py py2exe
"""

from setuptools import setup

APP = ['index.py']
DATA_FILES = ['icon.jpeg']
OPTIONS = {
    "iconfile": "icon.jpeg"
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2exe': OPTIONS},
    setup_requires=['py2exe'],
    name="Discord Mafia Advertising"
)
