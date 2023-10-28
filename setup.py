from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in migration_data_analysis/__init__.py
from migration_data_analysis import __version__ as version

setup(
	name="migration_data_analysis",
	version=version,
	description="Reports",
	author="Quentbit Technologies",
	author_email="contact@erpdata.in",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
