import unittest
def greater_than_five(val: int) -> bool:
    """
    Check if value > 5
    :param val: value to check.
    :return: True if value > 5, else - False
    """
    return val > 5
class Test(unittest.TestCase):
    def test(self):
        self.assertTrue(greater_than_five(6))
        self.assertFalse(greater_than_five(4))
if __name__ == "__main__":
    unittest.main()
