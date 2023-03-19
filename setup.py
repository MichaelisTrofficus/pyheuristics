"""
Run setup
"""

from setuptools import setup, find_packages


def parse_description(description):
    """
    Strip figures and alt text from description
    """
    return "\n".join(
        [
            a
            for a in description.split("\n")
            if ("figure::" not in a) and (":alt:" not in a)
        ]
    )


DISTNAME = "pyheuristics"
VERSION = "0.0.1"
DESCRIPTION = "A metaheuristics toolkit implemented in Python"
with open("README.md") as f:
    LONG_DESCRIPTION = parse_description(f.read())
CLASSIFIERS = [
    "Intended Audience :: Developers",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "Topic :: Scientific/Engineering",
]
AUTHOR = "Miguel Otero Pedrido"
AUTHOR_EMAIL = "miguel.otero.pedrido.1993@gmail.com"
LICENSE = "Apache 2.0"
PROJECT_URLS = {"Source Code": "https://github.com/MichaelisTrofficus/pyheuristics"}
MIN_PYTHON_VERSION = "3.8"

tests_require = [
    "pytest",
    "coverage",
    "nox",
]

setup(
    name=DISTNAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    classifiers=CLASSIFIERS,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    license=LICENSE,
    project_urls=PROJECT_URLS,
    packages=find_packages(),
    python_requires=">={0}".format(MIN_PYTHON_VERSION),
    extras_require=dict(tests=tests_require),
)
