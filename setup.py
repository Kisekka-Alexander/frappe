from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in offences_management/__init__.py
from offences_management import __version__ as version

setup(
	name="offences_management",
	version=version,
	description="Offence Management System",
	author="Alexander",
	author_email="alex@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
