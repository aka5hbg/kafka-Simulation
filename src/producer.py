from kafka import KafkaProducer
import json
import random
import time

# Kafka producer setup (connect to localhost:9092, which is the exposed Kafka port)
producer = KafkaProducer(bootstrap_servers='localhost:9092', value_serializer=lambda v: json.dumps(v).encode('utf-8'))

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
while True:
    transaction = generate_transaction()
    producer.send('transactions', transaction)
    print(f"Produced transaction: {transaction}")
    time.sleep(2)  # simulate new transaction every 2 seconds


