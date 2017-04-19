#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import re

from setuptools import setup


install_requires = [
    'wagtail>=1.9,<2.0',
    'jsonfield>=2.0.1<3.0',
    'filepreviews>=2.0.2,<3.0',
    'django-model-utils>=3.0.0,<4.0'
]

tests_require = [
    'responses>=0.5.1,<1.0',
    'flake8>=3.3.0<4.0',
    'isort>=4.2.5,<5.0'
]


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
    long_description='See https://github.com/filepreviews/wagtail-filepreviews for details',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Framework :: Django',
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 1.9',
        'Framework :: Django :: 1.10',
        'Topic :: Internet :: WWW/HTTP :: Site Management',
    ],
    install_requires=install_requires,
    extras_require={
        'test': tests_require,
    }
)
