from setuptools import setup

setup(
    name="loris",
    version="1.0.0",
    description="",
    author="senpai-10",
    url="https://github.com/Senpai-10/loris",
    install_requires=["click>=3.0"],
    include_package_data=True,
    py_modules=["loris"],
    entry_points={"console_scripts": ["loris = loris:main"]},
)
