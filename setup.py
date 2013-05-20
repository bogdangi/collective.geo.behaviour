from setuptools import setup, find_packages
import os

version = '0.1'

setup(
    name='collective.geo.behaviour',
    version=version,
    description="collective.geo Dexterity integration",
    long_description=(
        open("README.rst").read() + "\n" +
        open(os.path.join("docs", "HISTORY.txt")).read()
    ),
    # Get more strings from
    # http://pypi.python.org/pypi?:action=list_classifiers
    classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
    ],
    keywords='',
    author='',
    author_email='',
    url='https://github.com/collective/collective.geo.behaviour',
    license='GPL',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['collective', 'collective.geo'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'plone.behavior',
        'plone.directives.form',
        'zope.schema',
        'zope.interface',
        'zope.component',
        'rwproperty',
        'pygeoif > 0.2',
        'collective.geo.geographer  > 1.7',
        'collective.z3cform.mapwidget > 0.1',
        # -*- Extra requirements: -*-
    ],
    entry_points="""
    # -*- Entry points: -*-

    [z3c.autoinclude.plugin]
    target = plone
    """,
)
