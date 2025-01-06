#!/bin/bash
docker exec -it Container kafka-streaming-pipeline-my-python-producer-1 kafka-topics \
  --create --bootstrap-server localhost:9092 \
  --replication-factor 1 --partitions 1 --topic processed-user-login
