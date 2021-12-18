import unittest


def method(arg1, arg2):
    return arg1 + arg2


class Test(unittest.TestCase):
    def test_method_1(self):
        self.assertEqual(3, method(1, 2))

    def test_method_2(self):
        self.assertTrue(method(2, 3) == 5)
        self.assertFalse(method(2, 3) != 5)


if __name__ == "__main__":
    unittest.main()
