FROM python:3.12-alpine

RUN pip install poetry

RUN poetry config virtualenvs.create false

WORKDIR /workspace

VOLUME ["/workspace"]

COPY . .