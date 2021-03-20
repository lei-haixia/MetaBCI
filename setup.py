# -*- coding: utf-8 -*-
import setuptools

with open("README.md", "rb", errors="ignore") as fh:
    long_description = fh.read().decode("utf-8")

setuptools.setup(
    name="brainda",
    version="0.1",
    author="swolf",
    author_email="swolfforever@gmail.com",
    description="A Library of Datasets and Algorithms for Brain-Computer Interface",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(),
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)