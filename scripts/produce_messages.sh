#!/bin/bash
docker exec -it kafka-streaming-pipeline_kafka_1 kafka-console-producer \
  --bootstrap-server localhost:9092 --topic user-login