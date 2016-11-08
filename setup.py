# -*- coding: utf-8 -*-

from setuptools import setup


with open('README.rst') as f:
    readme = f.read()

# with open('LICENSE') as f:
#     license = f.read()

license = "MIT"

setup(
    name='wordseg',
    version='0.0.1',
    description='Split #hashtags into an array of words (English)',
    long_description=readme,
    author='Wesley Roberts',
    author_email='me@jchook.com',
    url='https://github.com/jchook/wordseg',
    license=license,
    packages=['wordseg'],
    package_dir={'wordseg': 'wordseg'},
    package_data={'wordseg': ['dict.txt']},
    scripts=['bin/wordseg']
)