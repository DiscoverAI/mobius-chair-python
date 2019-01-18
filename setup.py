import setuptools

setuptools.setup(
    name='mobius_chair',
    version='0.0.1',
    author='Falco Winkler, Daniel Schruhl',
    author_email='falcowinkler@icloud.com',
    description='Library for managing versions of datasets or models.',
    long_description='''Version your datasets and models on any filesystem.
    Refer to github for documentation: https://github.com/DiscoverAI/mobius-chair-python''',
    url='https://github.com/DiscoverAI/mobius-chair-python',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries',
        'Intended Audience :: Developers'
    ],
)
