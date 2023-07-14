FROM python:3.11.4-slim

ENV POETRY_VERSION=1.5.1

RUN pip install "poetry==$POETRY_VERSION"

WORKDIR /opt/app

COPY pyproject.toml poetry.lock ./

RUN poetry config virtualenvs.create false \
    && poetry install --no-root

COPY . .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
