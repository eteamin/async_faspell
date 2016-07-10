# -*- coding: utf-8 -*-

try:
    import logging
    import multiprocessing
except:
    pass

import sys
py_version = sys.version_info[:2]

try:
    from setuptools import setup, find_packages
except ImportError:
    from setuptools import setup, find_packages

packages = [
    'faspell'
]

requires = []

test_requirements = []
setup(
    name='faspell',
    version='0.1.0',
    description='Persian Spell_Checker in Python',
    author='eteamin',
    author_email='aminetesamian1371@gmail.com',
    url='https://github.com/eteamin/faspell',
    packages=packages,
    install_requires=requires,
    include_package_data=True,
    test_suite='nose.collector',
    tests_require=test_requirements,

)
