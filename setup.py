#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

import activeusers

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = activeusers.__version__

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    print("You probably want to also tag the version now:")
    print("  git tag -a %s -m 'version %s'" % (version, version))
    print("  git push --tags")
    sys.exit()

readme = open('README.md').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')
classifiers = [c for c in open('classifiers').read().splitlines() if '#' not in c]

setup(
    name='django-activeusers',
    version=version,
    description="""Your project description goes here""",
    long_description=readme + '\n\n' + history,
    author='arteria GmbH,Alvin Savoy',
    author_email='admin@arteria.ch',
    url='https://github.com/arteria/django-activeusers-tmp',
    packages=[
        'activeusers',
    ],
    include_package_data=True,
    install_requires=open('requirements.txt').read().splitlines(),
    license="MIT",
    zip_safe=False,
    keywords='django-activeusers-tmp',
    classifiers=classifiers,
)
