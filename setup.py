import io
import re

from setuptools import find_packages
from setuptools import setup

with io.open("README.rst", "rt", encoding="utf8") as f:
    readme = f.read()

with io.open("src/vocabulary_generator/__init__.py", "rt", encoding="utf8") as f:
    version = re.search(r'__version__ = "(.*?)"', f.read()).group(1)

setup(
    name='vocabulary_generator',
    version=version,
    project_urls={
        'Code': 'https://github.com/zakharovadaria/vocabulary_generator',
        'Issue tracker': 'https://github.com/zakharovadaria/vocabulary_generator/issues',
    },
    license='MIT',
    author='Daria Zakharova',
    author_email='zakharovadaria96@gmail.com',
    description='Simple search unknown words in text.',
    long_description=readme,
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    install_requires=[
        "nltk==3.4.5"
    ],
    extras_require={
        "dev": [
            "pytest",
        ],
    },
)
