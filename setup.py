#!/usr/bin/env python

from setuptools import setup, find_packages

packages = find_packages()
desc = open("README.md").read(),

setup(
    name='cooperhewitt.roboteyes.ascii',
    namespace_packages=['cooperhewitt', 'cooperhewitt.roboteyes'],
    version='0.2',
    description='',
    author='Cooper Hewitt Smithsonian Design Museum',
    url='https://github.com/cooperhewitt/py-cooperhewitt-roboteyes-ascii',
    requires=[
        'aalib'
    ],
    packages=packages,
    scripts=[],
    download_url='https://github.com/cooperhewitt/py-cooperhewitt-roboteyes-ascii/tarball/master',
    license='BSD')
