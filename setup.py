#!/usr/bin/env python

from setuptools import setup

with open('README.md', 'r') as f:
    long_desc = f.read()

with open('requirements.txt', 'r') as f:
    install_reqs = f.read().splitlines()

setup(
    name='armm',
    version='0.0a7',
    author='Andrew Nadolski',
    author_email='andrew.nadolski@gmail.com',
    description='Calculate mm-wave transmittance and reflectance of materials.',
    long_description=long_desc,
    long_description_content_type='text/markdown',
    platforms=['Linux', 'MacOS X'],
    url='https://github.com/anadolski/armm',
    install_requires=install_req,
    python_requires='>=3.6',
    package_dir={'armm': 'armm'},
    packages=['armm'],
    tests_require=['pytest'],
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX :: Linux',
        'Development Status :: 3 - Alpha',
        ],
    )
