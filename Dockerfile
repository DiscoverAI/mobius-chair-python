FROM circleci/python:3.6.8
COPY . /opt/mobius-chair-python
WORKDIR /opt/mobius-chair-python
USER root
RUN pipenv install -e . && pipenv install --dev
