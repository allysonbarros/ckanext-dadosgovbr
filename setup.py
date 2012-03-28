from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(
	name='ckanext-dadosgovbr',
	version=version,
	description="Custom CKAN extension for dados.gov.br website",
	long_description="""\
	""",
	classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
	keywords='',
	author='',
	author_email='',
	url='',
	license='',
	packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
	namespace_packages=['ckanext', 'ckanext.dadosgovbr'],
	include_package_data=True,
	zip_safe=False,
	install_requires=[
		# -*- Extra requirements: -*-
        'feedreader',
	],
	entry_points=\
	"""
        [ckan.plugins]
        dadosgovbr_theme=ckanext.dadosgovbr.plugin:DadosGovBrTheme
	""",
)
