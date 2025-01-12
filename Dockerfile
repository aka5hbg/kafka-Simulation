FROM python:3.8-slim

WORKDIR /app

COPY src/producer.py .

RUN pip install confluent-kafka kafka-python-ng

CMD ["python", "producer.py"]
