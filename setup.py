#!usr/bin/env python

from setuptools import setup, find_packages

setup(name="pig",
	version="0.2",
	description="Test for pip install git+",
	url="http://ss-nextpf.jp.fujitsu.com/FJH_project/gitlab/HTK.hanyu/hanyu_test.git",
	packages=find_packages(),
	entry_points="""
	[console_scripts]
	pig = pig.pig:main
	""",
	)
