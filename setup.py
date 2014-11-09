try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='systemlookup',
    version='0.0.1',
    author='Katja Hahn',
    author_email='struppigel@googlemail.com',
    packages=['systemlookup'],
    url='http://github.com/katjahahn/SystemLookup',
    license='Apache License 2.0',
    description='Command line tool to get info about filenames, clsid etc, from SystemLookup.com',
    long_description=open('README.md').read(),
    install_requires=[
        "beautifulsoup4 >= 4.2.0",
        "argparse == 1.2.1",
    ]
)
