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

  def test_invalid_credit_card(self):
    rv = self.app.post('/validate', data=dict(creditcard='5133-3367-8912-3456'))
    assert b'5133-3367-8912-3456' in rv.data 
    assert b'false' in rv.data