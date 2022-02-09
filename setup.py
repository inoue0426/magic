import os
import shutil
import sys
from warnings import warn

from setuptools import setup

if sys.version_info.major != 3:
    raise RuntimeError("Magic requires Python 3")


setup(
    name="magicdpeerlab",
    version="0.1.1",
    description="MAGIC",
    author="",
    author_email="",
    package_dir={"": "src"},
    packages=["magicdpeerlab"],
    install_requires=[
        "numpy>=1.10.0",
        "pandas>=0.18.0",
        "scipy>=0.14.0",
        "matplotlib",
        "seaborn",
        "scikit-learn",
        "networkx",
        "fcsparser",
        "statsmodels",
        "tables",
    ],
    scripts=["src/magicdpeerlab/magic_gui.py", "src/magicdpeerlab/MAGIC.py"],
)


# get location of setup.py
setup_dir = os.path.dirname(os.path.realpath(__file__))
