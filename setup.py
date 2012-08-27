#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-

from setuptools import setup

setup(
    name = 'TracNewPageMacro',
    version = '0.1',
    packages = ['newpage'],
    package_data={ 'newpage' : [ 'templates/*.html', "htdocs/*.*" ] },
    author = "Benjamin Lau",
    description = "Macro to add a form to a wiki page for creating new pages",
    license = "BSD",
    keywords = "trac plugin macro wiki",
    url = "http://trac-hacks.org/wiki/NewPageMacro",
    classifiers = [
        'Framework :: Trac',
    ],
    
    entry_points = {
        'trac.plugins': [
            'newpage.macro = newpage.macro',
        ],
    },
)
