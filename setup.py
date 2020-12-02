import sys

from setuptools import find_packages
from setuptools import setup

assert sys.version_info[0] == 3 and sys.version_info[1] >= 5, "Requires Python 3.5 or newer"

setup(
    name="stnm",
    version="0.0.1",
    description="stacks node manager",
    long_description=open("README.md").read(),
    packages=find_packages(),
    install_requires=[
        "psutil==5.7.3",
        "toml==0.10.2",
        "tornado==6.1",
        "Flask==1.1.2"
    ],
    entry_points={
        "console_scripts": [
            "stnm=run:main"
        ]
    })
