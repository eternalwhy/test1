import os
import sys

from setuptools import setup

if sys.version_info < (3, 6):
    raise RuntimeError("test1 requires Python 3.6+")


setup(name='test1',
    version='0.1',
    description='test task',
    url='https://github.com/eternalwhy/test1/',
    author='eternalwhy',
    author_email='eternalwhy@yandex.ru',
    license='MIT',
    packages=['test1'],
    zip_safe=False)