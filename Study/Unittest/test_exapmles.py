import unittest

class Test_Company(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('setup method...')

    def test_A(self):
        print('test method in A')

    def test_B(self):
        print('test method in B')

    def test_C(self):
        print('test method in C')

    @classmethod
    def tearDownClass(cls):
        print('teardown method')


if __name__ == '__main__':
    unittest.main()