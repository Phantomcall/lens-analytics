from setuptools import setup, find_packages

setup(
    name="lens-analytics-analytics-py",
    version="0.1.0",
    description="Python client for the lens-analytics-analytics Stellar price indexer API",
    packages=find_packages(),
    python_requires=">=3.9",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)
