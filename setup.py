#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import re

from setuptools import setup


install_requires = [
    'wagtail>=1.9,<2.0',
    'jsonfield',
    'filepreviews'
]


def read(*paths):
    """
    Build a file path from paths and return the contents.
    """
    with open(os.path.join(*paths), 'r') as f:
        return f.read()


def get_version(package):
    """
    Return package version as listed in `__version__` in `init.py`.
    """
    init_py = open(os.path.join(package, '__init__.py')).read()
    return re.search("__version__ = ['\"]([^'\"]+)['\"]", init_py).group(1)


def get_packages(package):
    """
    Return root package and all sub-packages.
    """
    return [
        dirpath for dirpath, dirnames, filenames in os.walk(package)
        if os.path.exists(os.path.join(dirpath, '__init__.py'))
    ]


setup(
    name='wagtaildocs_previews',
    version=get_version('wagtaildocs_previews'),
    description=(
        'Extend Wagtail\'s Documents with image previews and '
        'metadata from FilePreviews'
    ),
    author='José Padilla',
    author_email='jpadilla@filepreviews.io',
    url='https://github.com/filepreviews/wagtail-filepreviews',
    packages=get_packages('wagtaildocs_previews'),
    license='MIT',
    long_description=read('README.rst'),
    install_requires=install_requires
)
