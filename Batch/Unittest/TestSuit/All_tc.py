#test_suit file
import unittest
from Package1.test_login import LoginTest
from Package1.test_signup import SignUpTest
from Package2.test_payment import PaymentTest
from Package2.test_certificate import CerficateTest

t1=unittest.TestLoader().loadTestsFromTestCase(LoginTest)
t2=unittest.TestLoader().loadTestsFromTestCase(SignUpTest)
t3=unittest.TestLoader().loadTestsFromTestCase(PaymentTest)
t4=unittest.TestLoader().loadTestsFromTestCase(CerficateTest)

santitysuit=unittest.TestSuite([t1,t2])
functionalsuit=unittest.TestSuite([t3,t4])
mastersuit=unittest.TestSuite([t1,t2,t3,t4])

unittest.TextTestRunner().run(santitysuit)