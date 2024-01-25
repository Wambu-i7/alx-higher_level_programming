import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    def test_init_with_id(self):
        # Test initializing with provided id
        obj = Base(id=5)
        self.assertEqual(obj.id, 5)

    def test_init_without_id(self):
        # Test initializing without provided id
        obj1 = Base()
        obj2 = Base()
        self.assertEqual(obj1.id, 1)  # First instance should have id 1
        self.assertEqual(obj2.id, 2)  # Second instance should have id 2

if __name__ == '__main__':
    unittest.main()
