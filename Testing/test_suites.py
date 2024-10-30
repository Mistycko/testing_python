import unittest

from test_bank_account import bankAccountTest

def bank_account_suite():
    suite = unittest.TestSuite()
    suite.addTest(bankAccountTest("test_deposit"))
    suite.addTest(bankAccountTest("test_withdraw"))
    return suite


if __name__ == "__main__":
    runner= unittest.TextTestRunner()
    runner.run(bank_account_suite())