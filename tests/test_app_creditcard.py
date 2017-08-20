import os
import app_creditcard
import unittest
import tempfile

class AppCreditCardTestCase(unittest.TestCase):

  def setUp(self):
    app_creditcard.app.testing = True
    self.app = app_creditcard.app.test_client()

  def test_valid_credit_card(self):
    rv = self.app.post('/validate', data=dict(creditcard='4123456789123456'))
    assert b'4123456789123456' in rv.data 
    assert b'true' in rv.data

  # Must start with 4,5,6 (testing with 4)
  def test_valid_cc_start4(self):
    rv = self.app.post('/validate', data=dict(creditcard='4251-1127-8912-3456'))
    assert b'4251-1127-8912-3456' in rv.data 
    assert b'true' in rv.data

  # Must start with 4,5,6 (testing with 5)
  def test_valid_cc_start5(self):
    rv = self.app.post('/validate', data=dict(creditcard='5251-1127-8912-3456'))
    assert b'5251-1127-8912-3456' in rv.data 
    assert b'true' in rv.data

  # Must start with 4,5,6 (testing with 6)
  def test_valid_cc_start6(self):
    rv = self.app.post('/validate', data=dict(creditcard='6251-1127-8912-3456'))
    assert b'6251-1127-8912-3456' in rv.data 
    assert b'true' in rv.data

  # Case 1: 1111-xxxx-xxxx-xxxx
  def test_invalid_cc_case_1(self):
    rv = self.app.post('/validate', data=dict(creditcard='1111-3267-8912-3456'))
    assert b'1111-3267-8912-3456' in rv.data 
    assert b'false' in rv.data

  # Case 2: xx11-11xx-xxxx-xxxx
  def test_invalid_cc_case2(self):
    rv = self.app.post('/validate', data=dict(creditcard='5311-1167-8912-3456'))
    assert b'5311-1167-8912-3456' in rv.data 
    assert b'false' in rv.data

  # Case 3: x111-1xxx-xxxx-xxxx
  def test_invalid_cc_case3(self):
    rv = self.app.post('/validate', data=dict(creditcard='5111-1467-8912-3456'))
    assert b'5111-1467-8912-3456' in rv.data 
    assert b'false' in rv.data

  # Case 4: xxx1-111x-xxxx-xxxx
  def test_invalid_cc_case4(self):
    rv = self.app.post('/validate', data=dict(creditcard='5251-1117-8912-3456'))
    assert b'5251-1117-8912-3456' in rv.data 
    assert b'false' in rv.data

  # Case 5: Must start with 4,5,6
  def test_invalid_cc_case5(self):
    rv = self.app.post('/validate', data=dict(creditcard='0251-1117-8912-3456'))
    assert b'0251-1117-8912-3456' in rv.data 
    assert b'false' in rv.data

  # Case 6: Must have 16 digits
  def test_invalid_cc_case6(self):
    rv = self.app.post('/validate', data=dict(creditcard='4251-1317-8912-34565'))
    assert b'4251-1317-8912-34565' in rv.data 
    assert b'false' in rv.data

  # Case 7: Separators - wrong
  def test_invalid_cc_case7(self):
    rv = self.app.post('/validate', data=dict(creditcard='42-511317-8912-3456'))
    assert b'42-511317-8912-3456' in rv.data 
    assert b'false' in rv.data

  # Case 8: 17 digits without hyphen
  def test_invalid_cc_case8(self):
    rv = self.app.post('/validate', data=dict(creditcard='42536258796157867'))
    assert b'42536258796157867' in rv.data 
    assert b'false' in rv.data

  # Case 9: non-digits 
  def test_invalid_cc_case9(self):
    rv = self.app.post('/validate', data=dict(creditcard='44244x4424442444'))
    assert b'44244x4424442444' in rv.data 
    assert b'false' in rv.data

  # Case 10: separators with spaces
  def test_invalid_cc_case10(self):
    rv = self.app.post('/validate', data=dict(creditcard='5122-2368-7954 - 3214'))
    assert b'5122-2368-7954 - 3214' in rv.data 
    assert b'false' in rv.data

