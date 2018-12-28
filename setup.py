import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="metron",
    version="0.0.1",
    author="Falco Winkler",
    author_email="falcowinkler@icloud.com",
    description="Client for mobius-chair, a dataset versioning scheme.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DiscoverAI/metron",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)