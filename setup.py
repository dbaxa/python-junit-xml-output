#!/usr/bin/env python
from setuptools import setup, find_packages
import os

def read(fname):
	return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(name='junit_xml_output',
	author='David Black',
	author_email='dblack@atlassian.com',
	url='https://bitbucket.org/db_atlass/python-junit-xml-output-module',
	packages=find_packages(),
	description=read('README.md'),
	long_description=read('README.md'),
	license = "MIT",
	version = "0.0.1"
	)

