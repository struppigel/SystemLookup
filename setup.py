import os
from distutils.core import setup

long_description = 'Command line tool to get info about filenames, clsid etc, from SystemLookup.com'
if os.path.exists('README.txt'):
        long_description = open('README.txt').read()

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='systemlookup',
    version='0.0.4',
    author='Karsten Hahn',
    author_email='struppigel@googlemail.com',
    packages=['systemlookup'],
    url='http://github.com/katjahahn/SystemLookup',
    download_url = 'https://github.com/katjahahn/systemlookup/tarball/0.0.4',
    license='Apache License 2.0',
    platforms = ['any'],
    classifiers = ['Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Science/Research',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Topic :: Internet :: Log Analysis',
        'Topic :: System',
        'Programming Language :: Python'],
    description='Command line tool to get info about filenames, clsid etc, from SystemLookup.com',
    entry_points={
        'console_scripts': [
            'systemlookup = systemlookup.systemlookup:main'
        ]
    },
    keywords = ['systemlookup', 'malware research', 'malware', 'file info'],
    install_requires=[
        "beautifulsoup4 == 4.3.2",
        "requests == 2.4.3",
        "argparse == 1.2.1",
	"pyandoc == 0.2.0"
    ]
)
