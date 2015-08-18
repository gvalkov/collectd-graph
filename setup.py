#!/usr/bin/env python
# encoding: utf-8

from setuptools import setup
from collectd_graph import __version__


classifiers = [
    'Environment :: Console',
    'Topic :: Utilities',
    'Operating System :: OS Independent',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.1',
    'Programming Language :: Python :: 3.2',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'License :: OSI Approved :: MIT License',
    'Development Status :: 5 - Production/Stable',
]

entry_points = {
    'console_scripts': ['collectd-graph = collectd_graph.__main__:_main']
}

kw = {
    'name':             'collectd-graph',
    'version':          __version__,
    'description':      'Graphing utility for the collectd rrdtool plugin',
    'long_description': open('README.rst').read(),
    'author':           'Georgi Valkov',
    'author_email':     'georgi.t.valkov@gmail.com',
    'license':          'MIT',
    'keywords':         'collectd rrd rrdgraph',
    'url':              'https://github.com/gvalkov/collectd-graph',
    'classifiers':      classifiers,
    'packages':         ['collectd_graph'],
    'install_requires': [],
    'entry_points':     entry_points,
    'data_files':       [],
    'zip_safe':         True,
}

if __name__ == '__main__':
    setup(**kw)
