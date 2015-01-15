"""
UEC Syllabus
============

UEC Syllabus is a library to search syllabus.

search syllabus
------------

.. code:: python

    import calendar
    from uecsyllabus import Finder, Cource, Department

    finder = Finder()
    course = Cource(Development.INFOMATICS_ENGINEERING, evening=False)
    condition = dict(
        year=2014,
        course=course,
        semester=None,
        grade=2,
    )
    syllabuses = finder.search(condition)

"""
from __future__ import print_function
from setuptools import setup

setup(
    name='UEC Syllabus',
    version='0.1.0',
    url='http://github.com/pjxiao/uecsyllabus/',
    license='MIT',
    author='Takayuki Hirai',
    author_email='gen@pjxiao.net',
    description='UEC Syllabus is a library to search syllabus',
    long_description=__doc__,
    packages=['uecsyllabus'],
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=[
        "six",
        "enum34",
        "html5lib",
        "requests",
        "beautifulsoup4",
    ],
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
