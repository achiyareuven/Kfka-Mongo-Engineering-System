FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt requirements.txt

COPY ./docker_enricher .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8004

CMD ["python", "main.py"]

