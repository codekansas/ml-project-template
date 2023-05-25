#!/usr/bin/env python
"""Setup script for the project."""

import re

from setuptools import setup

PROJECT_NAME = "project"


with open("README.md", "r", encoding="utf-8") as f:
    long_description: str = f.read()


with open("requirements.txt", "r", encoding="utf-8") as f:
    requirements: list[str] = f.read().splitlines()


with open("requirements-dev.txt", "r", encoding="utf-8") as f:
    requirements_dev: list[str] = f.read().splitlines()


with open(f"{PROJECT_NAME}/__init__.py", "r", encoding="utf-8") as fh:
    version_re = re.search(r"^__version__ = \"([^\"]*)\"", fh.read(), re.MULTILINE)
assert version_re is not None, f"Could not find version in {PROJECT_NAME}/__init__.py"
version: str = version_re.group(1)


setup(
    name="ml-project",
    version=version,
    description="Template repository for ML projects",
    author="Benjamin Bolte",
    url="https://github.com/codekansas/ml-project-template",
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires=">=3.10",
    setup_requires=["cmake", "mypy", "pybind11", "torch"],
    install_requires=requirements,
    tests_require=requirements_dev,
    extras_require={"dev": requirements_dev},
)
