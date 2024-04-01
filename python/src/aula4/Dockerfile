FROM python:3.12

RUN pip install poetry

RUN poetry config virtualenvs.create false

WORKDIR /workspace

COPY ./src .