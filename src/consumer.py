import json
from confluent_kafka import Consumer, KafkaException
from config.consumer_config import CONSUMER_CONF
from utils.data_processing import process_message
from producer import send_to_kafka

# Kafka Consumer Initialization
consumer = Consumer(CONSUMER_CONF)
SOURCE_TOPIC = "user-login"

def main():
    consumer.subscribe([SOURCE_TOPIC])
    print("Starting Kafka consumer...")

    try:
        while True:
            msg = consumer.poll(1.0)
            if msg is None:
                continue
            if msg.error():
                if msg.error().code() == KafkaException._PARTITION_EOF:
                    print("End of partition reached")
                elif msg.error():
                    raise KafkaException(msg.error())
            else:
                processed_data = process_message(msg.value().decode('utf-8'))
                if processed_data:
                    send_to_kafka(processed_data)

    except KeyboardInterrupt:
        print("Consumer interrupted")
    finally:
        consumer.close()

if __name__ == "__main__":
    main()
