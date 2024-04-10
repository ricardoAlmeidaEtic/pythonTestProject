# Dockerfile
FROM python:3.10

RUN pip install poetry

RUN poetry config virtualenvs.create false

WORKDIR /workspace

VOLUME [ "/workspace" ]

COPY . .

RUN poetry install

EXPOSE 8000

CMD ["poetry" , "run" , "python" , "-m" , "aula10.main"]