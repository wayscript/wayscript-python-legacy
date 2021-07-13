FROM python:3.8.11-buster
MAINTAINER Team WayScript <founders@wayscript.com>

ENV SRC_DIR /usr/local/src/project
WORKDIR ${SRC_DIR}

RUN pip3 install pipenv

COPY Pipfile Pipfile.lock ${SRC_DIR}/

RUN pipenv install --system --dev && \
    rm -rf /root/.cache/pip

COPY ./ ${SRC_DIR}/

COPY ./files/ /
RUN chmod u+x /usr/local/bin/*

