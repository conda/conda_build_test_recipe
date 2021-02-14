#!/usr/bin/env python
# -*- coding: utf-8 -*-
import versioneer

from setuptools import setup
import versioneer

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    # TODO: put package requirements here
]

test_requirements = [
    # TODO: put package test requirements here
]
setup(
    name='conda_version_test',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description="Conda version sorting test",
    long_description=readme + '\n\n' + history,
    author="Continuum Analytics",
    author_email='conda@continuum.io',
    url='https://github.com/conda/conda_version_test',
    packages=[
        'conda_version_test',
    ],
    package_dir={'conda_version_test':
                 'conda_version_test'},
    include_package_data=True,
    install_requires=requirements,
    license="BSD license",
    zip_safe=False,
    keywords='conda_version_test',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
