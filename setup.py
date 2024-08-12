from setuptools import setup, find_packages

setup(
    name='roulier',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        # Ajoutez ici les dépendances requises
    ],
    include_package_data=True,
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

version = open('VERSION').read().strip()

setup(
    name="roulier",
    version=version,
    packages=find_packages(),
    install_requires=['lxml', 'Jinja2', 'requests'],
    author="Hparfr <https://github.com/hparfr>",
    description="Label parcels without pain",
    include_package_data=True,
    package_data={'roulier': ['*.xml', '*.xsl', '*.zpl']},

))

