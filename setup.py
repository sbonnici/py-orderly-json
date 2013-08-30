
from setuptools import setup

setup(
    name='orderlyjson',
    version='0.1',
    description='A python implementation of Orderly JSON '
                'which includes a setup for easy installation',
    url='http://github.com/sbonnici/py-orderly-json',
    author='Stephen Bonnici',
    author_email='stephen.bonnici@uniblue.com',
    long_description=open('README.md').read(),
    packages=[
        'orderlyjson',
        'orderlyjson.antlr3',
        'orderlyjson.jsonschema',
        'orderlyjson.jsonschema.tests'
    ],
    package_data={
        '': ['README.md',],
        'orderlyjson': ['tools',],
    }
)