#!/usr/bin/env python

# Copyright (c) 2019 WayScript, Inc. All rights reserved.
# Licensed under the MIT License.

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="wayscript",
    version="0.0.1",
    author="Team WayScript",
    author_email="founders@wayscript.com",
    description="WayScript gives you flexible building blocks to seamlessly integrate, automate and host tools in the cloud.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=['requests>=2.21.0'],
    url="https://github.com/wayscript/wayscript-python",
    packages=['wayscript'],
    license='MIT',
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Science/Research",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Communications",
        "Topic :: Database",
        "Topic :: Office/Business",
        "Topic :: Utilities",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: Implementation :: CPython",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Natural Language :: English",
    ],
    keywords=['wayscript', 'productivity', 'software', 'superpowers', 'scripts', 'cloud', 'tools', 'backend',
              'visual', 'low-code', 'modules', 'trigger'],
    zip_safe=False,
)
