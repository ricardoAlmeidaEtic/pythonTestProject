FROM python:3-alpine

RUN pip install poetry

RUN python3 -m pip install -U py-cord

RUN python3 -m pip install python-dotenv

RUN python3 -m pip install pydantic

WORKDIR /workspace

COPY . /workspace/

RUN poetry install 

RUN poetry add click py-cord requests pydantic

RUN poetry add --dev pytest ruff black
