from bitpay.exceptions import *
from bitpay.client import Client
from httmock import HTTMock
import unittest

class TestClient(unittest.TestCase):
  def test_pair_code_check(self):
    """tests whether the pairing code is syntatically correct"""
    new_client = Client(api_uri="https://test.bitpay.com")
    with self.assertRaisesRegex(BitPayArgumentError, "pairing code is not legal"):
      new_client.pair_pos_client("abcd")

  def test_passes_errors_when_pairing(self):
    """web errors should be gracefully passed to the client"""
    new_client = Client()
    def a_request(url, request):
      return {'status_code': 403, 'content': b'{"error": "this is a 403 error"}'}
    with HTTMock(a_request):
      with self.assertRaisesRegex(BitPayBitPayError, "403: this is a 403 error"):
        new_client.pair_pos_client("a1B2c3d")

  def test_passes_errors_when_creating_invoice(self):
    """web errors should be gracefully passed to the client"""
    new_client = Client()
    def a_request(url, request):
      return {'status_code': 403, 'content': b'{"error": "this is a 403 error"}'}
    with HTTMock(a_request):
      with self.assertRaisesRegex(BitPayBitPayError, "403: this is a 403 error"):
        new_client.create_invoice({"price": 20, "currency": "USD"})

  def test_unsigned_request_rates(self):
    """tests whether the generic wrapper returns properly
       when asked for rates
    """
    new_client = Client()
    request = new_client.unsigned_request('/rates/EUR')
    self.assertIn('rate', request.json()['data'])
