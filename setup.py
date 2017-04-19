#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import re
import shutil
import sys

from setuptools import setup


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

version = get_version('wagtaildocs_previews')

if sys.argv[-1] == 'publish':
    os.system("python setup.py sdist bdist_wheel")
    os.system("twine upload dist/*")
    print("You probably want to also tag the version now:")
    print("  git tag -a %s -m 'version %s'" % (version, version))
    print("  git push --tags")
    shutil.rmtree('dist')
    shutil.rmtree('build')
    shutil.rmtree('wagtaildocs_previews.egg-info')
    sys.exit()


setup(
    name='wagtaildocs_previews',
    version=version,
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
