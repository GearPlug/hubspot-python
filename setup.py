import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(name='hubspot-python',
      version='0.1.0',
      description='HubSpot API written in python',
      long_description=read('README.md'),
      author='Lelia Rubiano',
      author_email='lrubiano5@gmail.com',
      url='https://github.com/GearPlug/hubspot-python.git',
      packages=['hubspot'],
      install_requires=[
          'requests',
      ],
      keywords=['hubspot', 'crm'],
      zip_safe=False,
      license='GPL',
     )