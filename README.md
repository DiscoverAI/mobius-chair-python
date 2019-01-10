# Mobius Chair (Python)

[![CircleCI](https://circleci.com/gh/DiscoverAI/mobius-chair-python.svg?style=svg)](https://circleci.com/gh/DiscoverAI/mobius-chair-python)

> The Mobius Chair is Metron's technological masterpiece and allows him to cross space-time and interdimensional barriers.
>
> -- http://dc.wikia.com/wiki/Mobius_Chair

A Python library for versioning data (datasets, models) on an HDFS. This can be used by Python applications.

 - The base folder name will be the name of the transformation
 - This folder contains numbered folders that denote the version of the transformation
 - each of those folders contains numbered folders where the number stands
 for the generation (every time new input data is used, a new folder is created on this level)
 - The folders numbered by generation contain the datasets
 - A _SUCCESS file within the folders numbered by generation denotes that the dataset already
 has been processed

For example, in the following structure,
`zipper/0001/0001/dataset.part.1.csv` is the latest, unprocessed dataset:

    .
    ├── ...
    ├── zipper
    │   ├── 0001                                # version of zipper/your data transformation
    │   ├──── 0001                              # First generation
    │   ├────── dataset.part.1.csv
    │   ├──── 0002                              # second generation (same transformation, new input data)
    │   ├────── dataset.part.1.csv
    │   ├────── _SUCCESS
    │   ├── 0002                                # second version of transformation
    └── ...

## Install
Make sure you have pipenv and python 3.6 installed.

Then just run:
```bash
pipenv install --dev
```

## Test
Test it with:
```bash
pipenv run pytest
```
