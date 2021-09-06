import os
import sys
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.md')).read()
CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()

requires = [
]

extras_require = dict(
    dev=[],
)


setup(
    name='neuro.utils',
    version='0.0.1',
    description='Brain Cells, man',
    long_description=README + '\n\n' + CHANGES,
    classifiers=[
        "Programming Language :: Python",
        "Topic :: Internet :: WWW/HTTP",
    ],
    author="Rebekka Purcell",
    author_email="rebekkapurcell5@gmail.com",
    dependency_links=[
    ],
    license="MIT https://en.wikipedia.org/wiki/MIT_License",
    url='http://github.com/electricneurons',
    keywords='neurons, KTaR',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=requires,
    extras_require=extras_require,
    tests_require=requires,
    test_suite="neuro.utils.tests",
    entry_points="""
        [console_scripts]
    """,
)
