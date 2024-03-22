FROM python:3.10

# Intall poetry
RUN pip install poetry

# Working directory
WORKDIR /api

# Copy source code
COPY ./src/ ./src/

CMD ["scriptname.py", "-flag"]