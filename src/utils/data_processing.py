import json

def process_message(message):
    try:
        data = json.loads(message)
        if data.get('locale') == 'US':  # Filter locale "US"
            return {
                "user_id": data.get("user_id"),
                "device_type": data.get("device_type"),
                "timestamp": data.get("timestamp"),
                "insight": "Filtered locale US"
            }
    except Exception as e:
        print(f"Error processing message: {e}")
    return None
