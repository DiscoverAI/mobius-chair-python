## metron

[![CircleCI](https://circleci.com/gh/DiscoverAI/metron.svg?style=svg)](https://circleci.com/gh/DiscoverAI/metron)

 > Metron is one of the good New Gods of New Genesis lead by Highfather.
 > He is the God of Knowledge and travels space and time in his Mobius Chair
 > as part of an endless quest to know everything.
 >
 > --http://dc.wikia.com/wiki/Metron

An application using [mobius-chair](https://github.com/meandor/mobius-chair)
writes versioned datasets to a filesystem in the following pattern.

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
    │   ├── 0001                                     # version of zipper/your data transformation
    │   ├──── 0001                              # First generation
    │   ├────── dataset.part.1.csv
    │   ├──── 0002                              # second generation (same transformation, new input data)
    │   ├────── dataset.part.1.csv
    │   ├────── _SUCCESS
    │   ├── 0002                                     # second version of transformation
    └── ...

Metron is the python client for this versioning scheme, allowing you to easily
find the latest, unprocessed version in a mobius-chair generated folder.

## Install
Make sure you have pipenv and python 3.6.0 installed.

Then just run:
```bash
pipenv install --dev
```

## Test
Test it with:
```bash
pipenv run pytest
```

## Run
Run it with:
```bash
pipenv run monty/main.py
```
