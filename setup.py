from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in grade/__init__.py
from grade import __version__ as version

setup(
	name="grade",
	version=version,
	description="This is The grade wise rate app",
	author="Quantbit",
	author_email="grade123@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
