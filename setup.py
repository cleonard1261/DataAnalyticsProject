#!/usr/bin/env python
# setup
# Setup script for Data Analytics Project
#
# Author: Chad Leonard <cl1008@georgetown.edu>
# Created: 20140405
#
# Copyright (C) 2014 Georgetown University
# For license information, see LICENSE.txt
#
# ID: setup.py [] cl1008@georgetown.edu $

"""
Setup script for DAProject
"""

##########################################################################
## Imports
##########################################################################

try:
    from setuptools import setup
    from setuptools import find_packages
except ImportError:
    raise ImportError("Could not import \"setuptools\"."
                      "Please install the setuptools package.")

##########################################################################
## Package Information
##########################################################################

packages = find_packages(where=".", exclude=("tests", "bin", "docs", "fixtures",))
requires = []

with open('requirements.txt', 'r') as reqfile:
    for line in reqfile:
        requires.append(line.strip())

classifiers = (
    # TODO: Add classifiers
    # See: https://pypi.python.org/pypi?%3Aaction=list_classifiers
)

config = {
    "name": "daproject",
    "version": "0.1",
    "description": "Project: DC Crime and 311 calls analysis",
    "author": "Chad Leonard",
    "author_email": "cl1008@georgetown.edu",
    "url": "https://github.com/cleonard1261/DataAnalyticsProject",
    "packages": packages,
    "install_requires": requires,
    "classifiers": classifiers,
    "zip_safe": False,
    "scripts": ["scripts/gtcal",],
}

##########################################################################
## Run setup script
##########################################################################

if __name__ == '__main__':
    setup(**config)

    Status
    API
    Training
    Shop
    Blog
    About

    © 2014 GitHub, Inc.
    Terms
    Privacy
    Security
    Contact

