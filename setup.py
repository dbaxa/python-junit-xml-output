#!/usr/bin/env python
from setuptools import setup, find_packages
import os

def read(fname):
	return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(name='python-junit-xml-output-module',
	author='David Black',
	author_email='dblack@atlassian.com',
	url='https://bitbucket.org/db_atlass/python-junit-xml-output-module',
	packages=find_packages(),
	description=read('README'),
	long_description=read('README'),
	version = "0.0.1"
	)

