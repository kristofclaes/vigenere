#!/usr/bin/env python
# -*- coding: utf-8 -*-
import codecs
import re
from os.path import dirname, join, abspath

from setuptools import find_packages, setup

NAME = 'vigenere'
PACKAGES = find_packages(where='src')
META_PATH = join('src', 'vigenere', '__init__.py')
KEYWORDS = ['encryption']
CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: MacOS :: MacOS X',
    'Operating System :: Unix',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3.5',
    'Topic :: Security :: Cryptography'
]
INSTALL_REQUIRES = []

HERE = abspath(dirname(__file__))


def read(*parts):
    """
    Build an absolute path from `parts` and return the contents of the resulting file.
    """
    with codecs.open(join(HERE, *parts), 'rb', 'utf-8') as f:
        return f.read()


META_FILE = read(META_PATH)


def find_meta(meta):
    """
    Extract __*meta*__ from META_FILE.
    """
    meta_match = re.search(
        r'^__{meta}__ = [\'"]([^\'"]*)[\'"]'.format(meta=meta),
        META_FILE, re.M
    )
    if meta_match:
        return meta_match.group(1)
    raise RuntimeError('Unable to find __{meta}__ string.'.format(meta=meta))


if __name__ == '__main__':
    setup(
        name=NAME,
        description=find_meta('description'),
        license=find_meta('license'),
        url=find_meta('uri'),
        version=find_meta('version'),
        author=find_meta("author"),
        author_email=find_meta("email"),
        maintainer=find_meta("author"),
        maintainer_email=find_meta("email"),
        keywords=KEYWORDS,
        packages=PACKAGES,
        package_dir={"": "src"},
        zip_safe=False,
        classifiers=CLASSIFIERS,
        install_requires=INSTALL_REQUIRES,
    )
