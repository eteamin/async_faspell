# -*- coding: utf-8 -*-

try:
    import logging
    import multiprocessing
except:
    pass

try:
    from setuptools import setup, find_packages
except ImportError:
    from setuptools import setup, find_packages

packages = [
    'async_faspell',
]

requires = [
    'aiofiles'
]

test_requirements = []
setup(
    name='async_faspell',
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
