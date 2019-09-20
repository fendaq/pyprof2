#!/usr/bin/env python3

from setuptools import setup

with open('requirements.txt', 'r') as f:
	required = f.read().splitlines()

setup(
	name="pyprof2",
	version='1.0',
	author="Aditya Agrawal, Marek Kolodziej",
	author_email="aditya.iitb@gmail.com, mkolod@gmail.com",
	maintainer="Aditya Agrawal",
	maintainer_email="aditya.iitb@gmail.com",
	url="https://github.com/adityaiitb/pyprof2",
	license="BSD 3-Clause License",
	packages=['pyprof2',],
	install_requires=required,
)
