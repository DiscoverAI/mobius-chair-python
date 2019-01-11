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
Automated tests only run against a local filesystem.

## Connecting to hdfs

In function calls to the library, mobius-chair expects
a file system object.

This object has to support

    isdir(path)
    delete(path)
    ls(path)
    pathsep
    mkdir(path, create_parents=True)

The library was designed to use a filesystem object
that conforms to
[the abstraction in the `pyarrow` library](https://github.com/apache/arrow/blob/9178ad8c3c9ea371c3b7edb3fcee3073f5082bdc/python/pyarrow/filesystem.py#L29).
So, you can set up a hdfs cluster connection as described [here](https://arrow.apache.org/docs/python/filesystems.html)

```python
import mobius_chair.core as mc
fs = pyarrow.hdfs.connect(host, port, user=user, kerb_ticket=ticket_cache_path,
                driver='libhdfs3')
# or
fs = pyarrow.LocalFileSystem()
fs.delete = lambda x: shutil.rmtree(x)

mc.output_path(fs, "/test", "my-app", version=1)
```