import unittest
from src.utils.data_processing import process_message

class TestPipeline(unittest.TestCase):
    def test_process_message_valid(self):
        message = '{"user_id": "123", "locale": "US", "device_type": "android", "timestamp": "123456"}'
        result = process_message(message)
        self.assertIsNotNone(result)
        self.assertEqual(result["insight"], "Filtered locale US")

    def test_process_message_invalid(self):
        message = '{"user_id": "123", "locale": "RU", "device_type": "ios", "timestamp": "123456"}'
        result = process_message(message)
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()
