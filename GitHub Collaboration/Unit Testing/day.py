import main 
import unittest

class test_day1(unittest.TestCase):
    def test_add(self):
        result = main.add(2,2)
        self.assertEqual(result,4)

        result = main.add(-2,2)
        self.assertEqual(result,0) 

        result = main.add(-2,-2)
        self.assertEqual(result,- 4)

if __name__ == "__main__":
    unittest.main()