#!/usr/bin/env python

from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='aws-lambda-utils',
    version='0.0.2',
    description='AWS Lambda Function Python utilities',
    long_description=long_description,
    url='https://github.com/agassner/aws-lambda-utils',
    author='Arthur Gassner',
    author_email='arthur.gassner@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='aws lambda function utilities',
    packages=find_packages(exclude=['tests']),
    install_requires=['boto3'],
    extras_require={
    },
    package_data={
    },
    data_files=[],
    entry_points={
    },
)
