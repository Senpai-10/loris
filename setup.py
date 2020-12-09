from setuptools import setup
from setuptools.command.test import test as TestCommand



setup(
    name='loris',
    version=1.0.0,
    description='',
    author='senpai-10',
    url='https://github.com/Senpai-10/loris',
    install_requires=[],
    include_package_data=True,
    py_modules=["loris"],
    entry_points={
        'console_scripts': [
            "loris = loris:main"
        ]
    }
)
