from confluent_kafka import Producer
import os
import json
import time
import uuid
import random
from kafka.admin import KafkaAdminClient, NewTopic

# Kafka producer setup (connect to kafka:9093, which is the internal Kafka port)
bootstrap_servers = os.environ.get('BOOTSTRAP_SERVERS', 'localhost:9092')
topic = os.environ.get('KAFKA_TOPIC', 'Transcations')

# Create a Kafka producer configuration
producer_config = {
    'bootstrap.servers': bootstrap_servers,
}

# Create a Kafka producer instance
producer = Producer(producer_config)

# Simulate a financial transaction
def generate_transaction():
    transaction = {
        "transaction_id": random.randint(1000, 9999),
        "user_id": random.randint(1, 50),
        "amount": random.uniform(10, 5000),
        "transaction_type": random.choice(["debit", "credit"]),
        "location": random.choice(["USA", "Canada", "UK", "India"]),
        "timestamp": time.time(),
    }
    return transaction

# Produce messages to Kafka
try:
    while True:
        transaction = generate_transaction()
        # Serialize the transaction to JSON and encode it to bytes
        transaction_json = json.dumps(transaction).encode('utf-8')
        producer.produce(topic, transaction_json)
        producer.flush()
        print(f"Produced transaction: {transaction}")
        time.sleep(2)  # simulate new transaction every 2 seconds

except KeyboardInterrupt:
    pass

# Close the Kafka producer
producer.flush(30)
producer.close()