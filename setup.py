from setuptools import setup
from setuptools.command.test import test as TestCommand



setup(
    name='pypi-cli',
    version=__version__,
    description='A command-line interface to the Python Package Index (PyPI).',
    long_description=(read('README.rst') + '\n\n' +
                      read('CHANGELOG.rst')),
    author='Steven Loria',
    author_email='sloria1@gmail.com',
    url='https://github.com/sloria/pypi-cli',
    install_requires=REQUIRES,
    license=read("LICENSE"),
    zip_safe=False,
    include_package_data=True,
    keywords='pypi cli command line pipstat pip statistics download count metrics analytics',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: CPython',
    ],
    py_modules=["pypi_cli"],
    entry_points={
        'console_scripts': [
            "pypi = pypi_cli:cli"
        ]
    },
    tests_require=TESTS_REQUIRE,
    cmdclass={'test': PyTest}
)
