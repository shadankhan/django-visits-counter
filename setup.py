#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import sys, os
import visits_counter

setup(
    name='django-visits-counter',
    version=visits_counter.get_version(),
    description="Basic visit to object counter for Django",
    long_description=open('README.rst', 'r').read(),
    keywords='django, visit, counter, visitors',
    author='Jesús Espino García',
    author_email='jespinog at gmail dot com',
    url='http://code.google.com/p/django-visits-counter/',
    license='LGPL',
    package_dir={'visits_counter': 'visits_counter'},
    include_package_data=True,
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Internet :: Log Analysis",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content :: Page Counters",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Middleware",
        "Topic :: System :: Monitoring",
        "Topic :: Utilities",
    ]
)
