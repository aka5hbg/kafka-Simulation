
import unittest
from src.utils.data_processing import process_data

class TestUtils(unittest.TestCase):
    def test_process_data(self):
        data = {"key": "value"}
        result = process_data(data)
        self.assertEqual(result, data)

if __name__ == '__main__':
    unittest.main()