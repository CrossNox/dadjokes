from setuptools import setup
from dadjokes.constants import __version__


def readme():
    with open('README.md') as f:
        return f.read()


setup(
    name='dadjokes',
    version=__version__,
    description='icanhazdadjoke api wrapper',
    long_description=readme(),
    long_description_content_type="text/markdown",
    url='https://github.com/crossnox/dadjokes',
    author='CrossNox',
    packages=['dadjokes'],
    scripts=['script/dadjokes'],
    install_requires=['requests'],
    extras_require={'dev': ['bump']},
    classifiers=['Programming Language :: Python :: 3'],
)
