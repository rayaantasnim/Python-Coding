import unittest
from main2 import *

class Test_class(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(5, 3), 8)

    def test_subtract(self):
        self.assertNotEqual(subtract(10, 5), 10)

    def test_is_even_true(self):
        self.assertTrue(is_even(8))

    def test_is_even_false(self):
        self.assertFalse(is_even(7))
    
    def test_fruit_in_list(self):
        fruits = get_fruits()
        self.assertIn("banana", fruits)

    def test_student_instance(self):
        s = Student("Rayaan")
        self.assertIsInstance(s, Student)
    
    def test_div(self):
        with self.assertRaises(ZeroDivisionError):
            div(14,0)

if __name__ == "__main__":
    unittest.main()