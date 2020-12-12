from setuptools import setup, find_packages

with open('requirements.txt', 'r') as f:
    install_requires = f.readlines()

setup(name='Advent of Code 2020',
      author='Lukas Seifriedsberger',
      packages=find_packages(),
      install_requires=install_requires
      )
