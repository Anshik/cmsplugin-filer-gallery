# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import os
import cmsplugin_filer_gallery

CLASSIFIERS=[
    'Development Status :: 4 - Beta',
    'Environment :: Web Environment',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Framework :: Django'
]

setup(
    name='cmsplugin-filer-gallery',
    version=cmsplugin_filer_gallery.get_version(),
    description='Django CMS plugin for django-filer-gallery',
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.rst')).read(),
    author='Oyvind Saltvik',
    author_email='oyvind.saltvik@gmail.com',
    url='http://github.com/fivethreeo/cmsplugin-filer-gallery.git',
    packages=find_packages(),
    classifiers = CLASSIFIERS,
    test_suite = "cmsplugin_filer_gallery.test.run_tests.run_tests",
    include_package_data=True,
    zip_safe=False,
    install_requires=['django-cms', 'django-filer-gallery'],
)