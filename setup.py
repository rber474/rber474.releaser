# -*- coding: utf-8 -*-
"""Installer for the once.releaser package."""

from setuptools import find_packages
from setuptools import setup


long_description = '\n\n'.join([
    open('README.rst').read(),
    open('CONTRIBUTORS.rst').read(),
    open('CHANGES.rst').read(),
])


setup(
    name='once.releaser',
    version='1.0a1',
    description="Custom releaser hooks for ONCE project based on zest.releaser",
    long_description=long_description,
    # Get more from https://pypi.org/classifiers/
    classifiers=[
        "Environment :: Console",
        "Environment :: Plugins",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: System :: Archiving :: Packaging",
        "Topic :: System :: Installation/Setup",
        "Topic :: Utilities",
    ],
    keywords='Python Releaser',
    author='Rafael Bermúdez Horcajada',
    author_email='rber474@gmail.com',
    url='https://github.com/rber474/once.releaser',
    project_urls={
        'PyPI': 'https://pypi.org/project/once.releaser/',
        'Source': 'https://github.com/rber474/once.releaser',
        'Tracker': 'https://github.com/rber474/once.releaser/issues',
        # 'Documentation': 'https://once.releaser.readthedocs.io/en/latest/',
    },
    license='GPL version 2',
    packages=find_packages('src', exclude=['ez_setup']),
    namespace_packages=['once'],
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    python_requires=">=3.7",
    install_requires=[
        'setuptools',
        'zest.releaser',
        'zestreleaser.towncrier',
        'towncrier',
    ],
    extras_require={
        'test': [
            'plone.app.testing',
            # Plone KGS does not use this version, because it would break
            # Remove if your package shall be part of coredev.
            # plone_coredev tests as of 2016-04-01.
            'plone.testing>=5.0.0',
            'plone.app.contenttypes',
            'plone.app.robotframework[debug]',
        ],
    },
    entry_points={
        'zest.releaser.releaser.before':
            ['towncrier = once.releaser.towncrier:create_newsfile'],
    },
)
