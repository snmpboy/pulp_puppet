from setuptools import setup, find_packages

setup(
    name='pulp-puppet-devel',
    version='2.15.1',
    license='GPLv2+',
    packages=find_packages(exclude=['test', 'test.*']),
    author='Pulp Team',
    author_email='pulp-list@redhat.com'
)
