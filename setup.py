"""
poold.in
========

This is the application for the poold.in domain. It's only purpose is to
depend on pooldwww and possibly pooldrest, to support static resource builds
outside of heroku.

More to come as the news develops.
"""

import os
import sys
from setuptools import setup, find_packages


# Make sure the user can install poold.in code

username = os.environ.get('POOLDCODE_AUTH_USERNAME')
password = os.environ.get('POOLDCODE_AUTH_PASSWORD')

if not username:
    raise RuntimeError('A username is required to install poold.in packages')

if not password:
    raise RuntimeError('A password is required to install poold.in packages')


# Enforce python 2.7
py = sys.version_info[:2]

if py > (2, 7) or py < (2, 7):
    raise RuntimeError('Python 2.7 is required')


# Specify non-pypi dependency links (i.e. locate poold.in packages)
pooldin = 'http://%s:%s@code.poold.in/pypi/%s' % (username, password, '%s')
links = [
    pooldin % 'pooldwww/#egg==pooldwww',
]


# Required dependencies
required = [
    'pooldwww==0.1-dev.1350941856.a7923b2',
]


setup(name='poold.in',
      version='0.1',
      description='The poold.in website',
      long_description=__doc__,
      keywords='library',
      author='Poold.in',
      author_email='dev@poold.in',
      url='http://poold.in',
      license='PRIVATE',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=True,
      extras_require=dict(),
      install_requires=required,
      dependency_links=links,
      entry_points=dict(),
      scripts=[],
      classifiers=[
          'Development Status :: 4 - Beta',
          'Intended Audience :: Poold.in'
      ])
