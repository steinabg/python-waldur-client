#!/usr/bin/env python

from setuptools import find_packages, setup

install_requires = [
    "requests>=2.6.0",
]

tests_requires = [
    "responses>=0.5.0",
    "pytest>=6.2.5",
]

setup(
    name="python-waldur-client",
    version="0.1.0",
    author="OpenNode Team",
    author_email="info@opennodecloud.com",
    url="https://waldur.com",
    license="MIT",
    description="REST client for the Waldur API.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    install_requires=install_requires,
    tests_require=tests_requires,
    package_dir={"": "src"},
    packages=find_packages("src", exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: Integrators",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
