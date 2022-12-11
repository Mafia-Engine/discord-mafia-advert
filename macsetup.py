"""
Usage:
    python macsetup.py py2app
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
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
    name="Discord Mafia Advertising"
)
