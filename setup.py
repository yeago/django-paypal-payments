#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='django-paypal-payments',
    version='0.1',
    author='Steve Yeago',
    author_email='yeago999@gmail.com',
    description='django-paypal-payments',
    url='http://github.com/yeago/django-paypal-payments',
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Operating System :: OS Independent",
        "Topic :: Software Development"
    ],
)
