#! /usr/bin/env python

from distutils.core import setup
from youtube_dl_gui import version

setup(name='Youtube-DLG',
	version=version.__version__,
	description='Youtube-dl GUI',
	author='Sotiris Papadopoulos',
	author_email='ytubedlg@gmail.com',
	url='https://github.com/MrS0m30n3/youtube-dl-gui',
	packages=['youtube_dl_gui'])
