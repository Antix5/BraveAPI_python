from setuptools import setup, find_packages

setup(
    name='BraveAPI',
    version='0.1.0',
    description='A simple Python wrapper for the Brave API with additonal support for other tools (all in docs)',
    packages=["BraveAPI_python"],
    license='GPLv3',
    author='Antoine Demangeon',
    install_requires=[
        'requests',
    ],
)