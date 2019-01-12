# Mobius Chair (Python)

[![CircleCI](https://circleci.com/gh/DiscoverAI/mobius-chair-python.svg?style=svg)](https://circleci.com/gh/DiscoverAI/mobius-chair-python)

> The Mobius Chair is Metron's technological masterpiece and allows him to cross space-time and interdimensional barriers.
>
> -- http://dc.wikia.com/wiki/Mobius_Chair

A Python library for versioning data (datasets, models) on a Filesystem. This can be used by Python applications.

## How it works

 <p align="center">
  <img src="https://github.com/DiscoverAI/mobius-chair-python/raw/master/docu/mobius_chair_versioning.png" width="500">
</p>

In detail
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

## Connecting to a filesystem

In function calls to the library, mobius-chair expects
a file system object.

This object has to support

    isdir(path)
    delete(path)
    ls(path)
    pathsep
    mkdir(path, create_parents=True)

The library was designed to use a filesystem object that conforms to
[the abstraction in the `pyarrow` library](https://github.com/apache/arrow/blob/9178ad8c3c9ea371c3b7edb3fcee3073f5082bdc/python/pyarrow/filesystem.py#L29).
This means it supports HDFS out of the box.


## Try it out

Warning: pyarrow uses hadoop native libraries.
On unix systems they ship with a hadoop distribution,
on mac you need to [build hadoop from source](https://medium.com/@faizanahemad/hadoop-native-libraries-installation-on-mac-osx-d8338a6923db)

- Set up an hdfs as described [here](https://hadoop.apache.org/docs/r3.0.3/hadoop-project-dist/hadoop-common/SingleCluster.html)
- Install mobius_chair
  - (not ready yet) from pypi: ` pip install mobius_chair`)
  - from sources: python setup.py install --prefix=$HOME/.local
- Start versioning:

```python3
>>> import pyarrow as pa
>>> import mobius_chair.core as mc
>>> fs = pa.hdfs.connect("localhost", 9000)
>>> mc.output_path(fs, "/test", "zipper", 1)
﻿WARNING:root:Did not find latest generation
'/test/zipper/0001/0001'
```

## Dependencies
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
Automated tests only run against a local filesystem.