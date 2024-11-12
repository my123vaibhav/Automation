#test_signup.py
import unittest
class SignUpTest(unittest.TestCase):
    def test_signupbygmail(self):
        print('this tc is for gmail signup-')
    def test_signupbyphone(self):
        print('this tc is for phone signup')
    def test_signupbyfacebook(self):
        print('this tc is for facebook signup')
if __name__ == "__main__":
    unittest.main()