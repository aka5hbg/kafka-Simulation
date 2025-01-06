import json
from confluent_kafka import Producer
from config.producer_config import PRODUCER_CONF

# Kafka Producer Initialization
producer = Producer(PRODUCER_CONF)
TARGET_TOPIC = "processed-user-login"

def send_to_kafka(data):
    try:
        producer.produce(TARGET_TOPIC, json.dumps(data))
        producer.flush()
        print(f"Message sent to topic {TARGET_TOPIC}: {data}")
    except Exception as e:
        print(f"Error producing message: {e}")

