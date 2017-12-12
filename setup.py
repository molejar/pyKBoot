#!/usr/bin/env python

# Copyright 2015 Martin Olejar
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import sys
import kboot

from setuptools import setup, find_packages

requirements = ['click>=6.0', 'pyserial>=3.0']

if sys.platform.startswith('linux'):
    requirements.append('pyusb>=1.0.0b2')
elif sys.platform.startswith('win'):
    requirements.append('pywinusb>=0.4.0')
else:
    raise Exception('Not supported platform !')

setup(
    name='kboot',
    version=kboot.__version__,
    description='Python module for Kinetis Bootloader',
    author='Martin Olejar',
    author_email='martin.olejar@gmail.com',
    keywords="Kinetis bootloader",
    url="https://github.com/molejar/pyKBoot",
    license="Apache 2.0",
    platforms = "Mac OS X, Windows, Linux",
    classifiers = [
        'Programming Language :: Python',
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Topic :: Scientific/Engineering',
        'Topic :: Software Development :: Embedded Systems',
        'Topic :: Utilities',
    ],
    entry_points = {
        'console_scripts': [
            'kboot = kboot.tool:main',
        ],
    },
    packages=['kboot'],
    install_requires = requirements,
    include_package_data = True,
)
