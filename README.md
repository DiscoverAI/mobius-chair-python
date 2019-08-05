# Mobius Chair (Python)

[![CircleCI](https://circleci.com/gh/DiscoverAI/mobius-chair-python.svg?style=svg)](https://circleci.com/gh/DiscoverAI/mobius-chair-python)

> The Mobius Chair is Metron's technological masterpiece and allows him to cross space-time and interdimensional barriers.
>
> -- http://dc.wikia.com/wiki/Mobius_Chair

A Python library for versioning data (datasets, models) on a Filesystem. This can be used by Python applications.

## How it works

 <p align="center">
  <img src="https://github.com/DiscoverAI/mobius-chair-python/raw/master/docu/mobius_chair_versioning.png">
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

Mobius char supports only WebHDFS, for now.
In theory it supports every file system that can conform to that same
interface:

    delete(self, hdfs_path, recursive=False, skip_trash=True)
    list(self, hdfs_path, status=False)
    status(self, hdfs_path, strict=True)
    makedirs(self, hdfs_path, permission=None)
    walk(self, hdfs_path, depth=0, status=False, ignore_missing=False)

So if you write your own class and adapt these methods to your fs,
it can be supported as well.

## Try it out

- Set up an hdfs as described [here](https://hadoop.apache.org/docs/r3.0.3/hadoop-project-dist/hadoop-common/SingleCluster.html)
- Install mobius_chair
  - (not ready yet) from pypi: ` pip install mobius_chair`)
  - from sources: `python setup.py install`
- Start versioning:

```python3
>>> from hdfs import InsecureClient
>>> client = InsecureClient('http://localhost:50070', root='/')
>>> import mobius_chair.writer as mw
>>> mw.output_path(fs=client, base_path="", name="my_app", version=1)
WARNING:root:Did not find latest generation
'/my_app/0001/0001'
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

Unit tests only run against a local filesystem.
