from setuptools import setup
import os

PROJECT_ROOT, _ = os.path.split(__file__)
VERSION = REVISION = '0.0.1'
PROJECT_NAME = 'relationshipforest'
PROJECT_AUTHORS = "Salim Fadhley"
PROJECT_EMAILS = 'salimfadhley@gmail.com'
PROJECT_URL = "https://bitbucket.org/salimfadhley/pythonmoo"
SHORT_DESCRIPTION = 'Graphs of graphs of related things'

try:
    DESCRIPTION = open(os.path.join(PROJECT_ROOT, "README.rst")).read()
except IOError as _:
    DESCRIPTION = SHORT_DESCRIPTION

# Actual setup

setup(name=PROJECT_NAME.lower(),
      version=VERSION,
      author=PROJECT_AUTHORS,
      author_email=PROJECT_EMAILS,
      packages=["pythonmoo"],
      zip_safe=True,
      include_package_data=False,
      install_requires=['pyrsistent'],
      tests_requires=['mock',],
      url=PROJECT_URL,
      description=SHORT_DESCRIPTION,
      long_description=DESCRIPTION,
      )
