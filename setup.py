from setuptools import setup


setup(name='HubSpot',
      version='0.1',
      description='HubSpot API written in python',
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