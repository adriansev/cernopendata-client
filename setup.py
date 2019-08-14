# -*- coding: utf-8 -*-
# TODO: add Licence
"""cernopendata-client."""

import os
import re

from setuptools import setup

readme = open('README.rst').read()
history = open('CHANGES.rst').read()

tests_require = [
    'isort==4.3.4',
    'coverage>=4.0',
    'pydocstyle>=1.0.0',
    'pytest-cache>=1.0',
    'pytest-cov>=1.8.0',
    'pytest-pep8>=1.0.6',
    'pytest>=2.8.0',
]

extras_require = {
    'docs': [
        'Sphinx>=1.4.4,<2.0',
        'sphinx-rtd-theme>=0.1.9',
        'sphinx-click>=1.0.4',
    ],
    'tests': tests_require,
}

extras_require['all'] = []
for key, reqs in extras_require.items():
    if ':' == key[0]:
        continue
    extras_require['all'].extend(reqs)

setup_requires = [
    'pytest-runner>=2.7',
]

install_requires = [
    'click>=7,<8',
]

# Get the version string. Cannot be done with import!
with open(os.path.join('cernopendata_client', 'version.py'), 'rt') as f:
    version = re.search(
        '__version__\s*=\s*"(?P<version>.*)"\n',
        f.read()
    ).group('version')

setup(
    name='cernopendata-client',
    version=version,
    description=__doc__,
    long_description=readme + '\n\n' + history,
    author='CERN Open Data',
    author_email='', #TODO: add email
    packages=['cernopendata_client', ],
    extras_require=extras_require,
    install_requires=install_requires,
    setup_requires=setup_requires,
    tests_require=tests_require,
    entry_points={
        'console_scripts': [
            'cernopendata-client = cernopendata_client.cli:cernopendata_client'
        ]
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License', # TODO: check licence
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: System :: Archiving'
    ]
)
