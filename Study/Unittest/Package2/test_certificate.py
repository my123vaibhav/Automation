#test_cerrtificate
import unittest
class CerficateTest(unittest.TestCase):
    def test_certificatebyname(self):
        print('this tc is for name of vendor')
    def test_certificatebyformate(self):
        print('this tc is for pdf formate')

if __name__ == "__main__":
    unittest.main()