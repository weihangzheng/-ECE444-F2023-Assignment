import unittest
from utils import Utils  # Make sure utils.py is in the same directory as this file or adjust the import accordingly

class TestUtils(unittest.TestCase):
    
    def test_reversed(self):
        # Testing with integer input
        self.assertEqual(Utils.reversed(1234), 4321)
        
        # Testing with float input - expected to return error message
        self.assertEqual(Utils.reversed(1234.56), "Invalid input, please provide a valid integer")

        # Testing with string input - expected to return error message
        self.assertEqual(Utils.reversed("abcd"), "Invalid input, please provide a valid integer")

    def test_formatter(self):
        # Testing with integer input
        self.assertEqual(Utils.formatter(10), ('1010', '12'))
        
        # Testing with float input - expected to return error message
        self.assertEqual(Utils.formatter(1234.56), "Invalid input, please provide a valid integer")

        # Testing with string input - expected to return error message
        self.assertEqual(Utils.formatter("abcd"), "Invalid input, please provide a valid integer")


if __name__ == "__main__":
    unittest.main()
