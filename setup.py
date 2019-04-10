from setuptools import setup


def readme():
  with open('README.rst') as f:
    return f.read()


setup(name='dadjokes',
      version='0.1',
      description='icanhazdadjoke api wrapper',
      long_description=readme(),
      url='https://github.com/crossnox/dadjokes',
      author='CrossNox',
      packages=['dadjokes'],
      # scripts=['script/dadjokes'],
      install_requires=['requests'],
      classifiers=[
          'Programming Language :: Python :: 3'
      ]
      )
