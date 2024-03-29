from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in techtrix_customisations/__init__.py
from techtrix_customisations import __version__ as version

setup(
	name="techtrix_customisations",
	version=version,
	description="Techtrix Customisations",
	author="TNS",
	author_email="furqan.79000@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
