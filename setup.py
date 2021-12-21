import os
import re
from setuptools import setup, find_packages


BASE_DIR = os.path.dirname(__file__)

PACKAGE_NAME = "connectmp"

SHORT_DESCRIPTION = "ConnectMP - The easiest and efficient way to share data between Processes. " \
                    "It's superfast, can handle big datas, cancreate `multiple` data connection and really " \
                    "simple to get started. 🍰"

LONG_DESCRIPTION_FILE_PATH = "README.md"

URL = "https://github.com/AidenEllis/ConnectMP"

PROJECT_URLS = {
    'Github': 'https://github.com/AidenEllis/ConnectMP',
    'Documentation': 'https://github.com/ConnectMP/',
    'Issue tracker': 'https://github.com/AidenEllis/ConnectMP/issues'
}

REQUIREMENTS_FILE_PATH = "requirements.txt"

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

KEYWORDS = [
    "ConnectMP",
    "process",
    "data",
    "sharing",
    "multiprocessing",
    "AidenEllis"
]

AUTHOR = "Aiden Ellis"
AUTHOR_EMAIL = "itsaidenellis@protonmail.com"

try:
    with open(os.path.join(BASE_DIR, 'connectmp', '__init__.py')) as f:
        version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE).group(1)
except AttributeError:
    raise RuntimeError("__version__ not found.")

if not version:
    raise RuntimeError('Verison not provided.')


def read_file(filename):
    with open(os.path.join(os.path.dirname(__file__), filename)) as file:
        return file.read()


setup(
    name=PACKAGE_NAME,
    version=version,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    license='MIT',
    long_description_content_type="text/markdown",
    long_description=read_file('README.md'),
    description=SHORT_DESCRIPTION,
    packages=find_packages(),
    url=URL,
    project_urls=PROJECT_URLS,
    install_requires=requirements,
    keywords=KEYWORDS,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ]
)