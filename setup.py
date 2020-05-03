import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="penut",
    version="0.0.3",
    author="PenutChen",
    author_email="penut85420@gmail.com",
    description="This is a collection of my useful functions.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/penut85420/Penut",
    packages=setuptools.find_packages(),
    install_requires=[
        "numpy", "pandas", "matplotlib"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
