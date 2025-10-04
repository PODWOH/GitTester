from setuptools import setup, find_packages

setup(
    name="my-python-package",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "numpy>=1.21.0",
        "requests>=2.25.0",
    ],
    python_requires=">=3.8",
)