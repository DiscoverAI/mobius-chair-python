import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mobius_chair",
    version="0.0.1",
    author="Falco Winkler",
    author_email="falcowinkler@icloud.com",
    description="Library for managing versions of datasets or models.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DiscoverAI/mobius-chair-python",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: APACHE 2.0 License",
        "Operating System :: OS Independent",
    ],
)