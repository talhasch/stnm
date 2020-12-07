import sys
from glob import glob

from setuptools import find_packages
from setuptools import setup

assert sys.version_info[0] == 3 and sys.version_info[1] >= 5, "Requires Python 3.5 or newer"

setup(
    name="stnm",
    version="0.2.1",
    author="Talha Buğra Bulut",
    author_email="talhabugrabulut@gmail.com",
    url="https://github.com/talhasch/stnm",
    description="Stacks blockchain node process manager",
    long_description="Stacks blockchain node process manager. See https://github.com/talhasch/stnm for mode details.",
    packages=find_packages(exclude=("venv",)),
    data_files=[
        ('web_static', glob('stnm/web/static/**/**')),
        ('web_templates', glob('stnm/web/templates/**/**')),
        # etc...
    ],
    install_requires=[
        "psutil==5.7.3",
        "toml==0.10.2",
        "tornado==6.1",
        "Flask==1.1.2"
    ],
    entry_points={
        "console_scripts": [
            "stnm=stnm.run:main"
        ]
    })
