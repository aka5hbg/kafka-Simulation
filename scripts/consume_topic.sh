#!/bin/bash
docker exec -it kafka-streaming-pipeline_kafka_1 kafka-console-consumer \
  --bootstrap-server localhost:9092 \
  --topic processed-user-login --from-beginning
