#test_payment
import unittest
class PaymentTest(unittest.TestCase):
    def test_paymentbydollor(self):
        print('this tc is for payment dollor')
    def test_paymentbyrupees(self):
        print('this tc is for payment by rupees')

if __name__ == "__main__":
    unittest.main()