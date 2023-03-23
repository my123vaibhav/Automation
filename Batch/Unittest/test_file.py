import unittest

class Test_Company(unittest.TestCase):
    @unittest.skipIf(1==1,'it is true')
    def test_Z(self):
        print('test method in Z')

    @unittest.skip
    def test_Z(self):
        print('test method in B')

    def test_Z(self):
        print('test method in C')

if __name__ == '__main__':
    unittest.main()