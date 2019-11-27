from setuptools import find_packages, setup

setup(
    name="{{ cookiecutter.repo_name.lower().replace('-', '_') }}",
    packages=find_packages(),
    version='0.1.0',
    description='{{ cookiecutter.description }}',
    author='Logan Rudd'
)
