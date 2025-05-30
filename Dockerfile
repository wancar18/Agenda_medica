FROM python:3.9-slim-buster

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    default-libmysqlclient-dev \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PYTHONPATH=/app

ENV FLASK_APP=app:app

CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]