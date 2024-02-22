from setuptools import setup,find_packages
from typing import List

with open('README.md','r',encoding='utf-8') as f:
    long_description =f.read()
    

__version__="0.0.4"
REPO_NAME ="MONGODB_PACKAGE"
PKG_NAME ="databaseautomation"
AUTHOR_NAME="MadhuMaayera"
AUTHOR_EMAIL="madhurimasit61@gmail.com"

setup(
    name=PKG_NAME,
    version=__version__,
    author= AUTHOR_NAME ,
    author_email= AUTHOR_EMAIL,
    description="My python package for connecting database",
    url=f"https://github.com/{AUTHOR_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker":f"https://github.com/{AUTHOR_NAME}/{REPO_NAME}/issues",
    },
    package_dir= {'': 'src'},
    packages=find_packages(where="src"),
)