from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in abcd_translator/__init__.py
from abcd_translator import __version__ as version

setup(
	name="abcd_translator",
	version=version,
	description="Replaces strings based from translation table",
	author="Jon Ronquillo",
	author_email="jon_ronquillo@yahoo.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
