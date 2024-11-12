#test_login.py
import unittest
class LoginTest(unittest.TestCase):
    def test_loginbygmail(self):
        print('this tc is for gmail login')
    def test_loginbyphone(self):
        print('this tc is for phone login')
    def test_loginbyfacebook(self):
        print('this tc is for facebook login')
if __name__== "__main__":
    unittest.main()