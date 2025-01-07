from kafka import KafkaConsumer
import json

# Kafka consumer setup
consumer = KafkaConsumer(
    'transactions',                         # Topic name
    bootstrap_servers='localhost:9092',     # Kafka broker address
    auto_offset_reset='earliest',           # Start from the beginning of the topic
    value_deserializer=lambda m: m.decode('utf-8') if m else None,  # Just decode the message without deserializing
    group_id='my-consumer-group'            # Consumer group ID
)

# Consume messages
print("Consumer started. Listening for messages...")
for message in consumer:
        try:
            parsed_message = json.loads(message.value)  # Try to load as JSON
            print(f"Parsed JSON message: {parsed_message}")
        except json.JSONDecodeError:
            print(f"Invalid JSON: {message.value}")  # Print invalid JSON
        except Exception as e:
            print(f"Unexpected error: {e}")
