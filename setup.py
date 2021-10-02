from setuptools import setup, find_packages

setup(
    version="0.1.0",
    name="lidl_plus",
    author="Nils Deters",
    description="Unofficial python client for the lidl plus api.",
    url="https://gitlab.com/nilsdet/lidl-plus-sdk",
    packages=find_packages(exclude=("tests",)),
    include_package_data=True,
    install_requires=["dacite~=1.6.0", "requests~=2.26.0"],
    platforms=["any"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.9",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
