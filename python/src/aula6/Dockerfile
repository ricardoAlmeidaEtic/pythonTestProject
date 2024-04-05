FROM python:3-alpine

RUN pip install poetry

RUN pip install discord.py

RUN pip install gtts

WORKDIR /workspace

COPY . /workspace/

RUN poetry install 
