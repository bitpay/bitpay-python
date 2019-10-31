from bitpay.exceptions import *
from bitpay import key_utils
import requests
import json
import re

class Client:
  def __init__(self, api_uri="https://bitpay.com", insecure=False, pem=key_utils.generate_pem(), tokens={}):
    self.uri = api_uri
    self.verify = not(insecure)
    self.pem = pem
    self.client_id = key_utils.get_sin_from_pem(pem)
    self.tokens = tokens
    self.user_agent = 'bitpay-python'

  def pair_pos_client(self, code):
    if re.match("^\w{7,7}$", code) is None:
      raise BitPayArgumentError("pairing code is not legal")
    payload = {'id': self.client_id, 'pairingCode': code}
    response = self.unsigned_request('/tokens', payload)
    if response.ok:
      self.tokens = self.token_from_response(response.json())
      return self.tokens 
    self.response_error(response)

  def create_token(self, facade):
    payload = {'id': self.client_id, 'facade': facade}
    response = self.unsigned_request('/tokens', payload)
    if response.ok:
      self.tokens = self.token_from_response(response.json())
      return response.json()['data'][0]['pairingCode']
    self.response_error(response)

  def create_invoice(self, params):
    self.verify_invoice_params(params['price'], params['currency'])
    payload = json.dumps(params)
    uri = self.uri + "/invoices"
    xidentity = key_utils.get_compressed_public_key_from_pem(self.pem)
    xsignature = key_utils.sign(uri + payload, self.pem)
    headers = {"content-type": "application/json", 'X-Identity': xidentity, 'X-Signature': xsignature, 'X-accept-version': '2.0.0'}
    try:
      response = requests.post(uri, data=payload, headers=headers, verify=self.verify)
    except Exception as pro:
      raise BitPayConnectionError(pro.args)
    if response.ok:
      return response.json()['data']
    self.response_error(response)

  def get_invoice(self, invoice_id, token=None):
    if token:
        uri = self.uri + "/invoices/" + invoice_id + "?token=" + token
        xidentity = key_utils.get_compressed_public_key_from_pem(self.pem)
        xsignature = key_utils.sign(uri, self.pem)
        headers = {"content-type": "application/json", 'X-Identity': xidentity, 'X-Signature': xsignature, 'X-accept-version': '2.0.0'}
    else:
        uri = self.uri + "/invoices/" + invoice_id
        headers = {"content-type": "application/json"}

    try:
      response = requests.get(uri, headers=headers, verify=self.verify)
    except Exception as pro:
      raise BitPayConnectionError(pro.args)
    if response.ok:
      return response.json()['data']
    self.response_error(response)

  def verify_tokens(self):
    """
    Deprecated, will be made private in 2.4
    """
    xidentity = key_utils.get_compressed_public_key_from_pem(self.pem)
    url = self.uri + "/tokens"
    xsignature = key_utils.sign(self.uri + "/tokens", self.pem)
    headers = {"content-type": "application/json", 'X-Identity': xidentity, 'X-Signature': xsignature, 'X-accept-version': '2.0.0'}
    response = requests.get(self.uri + "/tokens", headers=headers, verify=self.verify)
    if response.ok:
      allTokens = response.json()['data']
      selfKeys = self.tokens.keys() 
      matchedTokens = [token for token in allTokens for key in selfKeys if token.get(key) == self.tokens.get(key)]
      if not matchedTokens:
        return False
      return True

  def token_from_response(self, responseJson):
    """
    Deprecated, will be made private in 2.4
    """
    token = responseJson['data'][0]['token']
    facade = responseJson['data'][0]['facade']
    return {facade: token}
    raise BitPayBitPayError('%(code)d: %(message)s' % {'code': response.status_code, 'message': response.json()['error']})

  def verify_invoice_params(self, price, currency):
    """
    Deprecated, will be made private in 2.4
    """
    if re.match("^[A-Z]{3,3}$", currency) is None:
      raise BitPayArgumentError("Currency is invalid.")
    try: 
      float(price)
    except:
      raise BitPayArgumentError("Price must be formatted as a float")
  def response_error(self, response):
    raise BitPayBitPayError('%(code)d: %(message)s' % {'code': response.status_code, 'message': response.json()['error']})

  def unsigned_request(self, path, payload=None):
    """
    generic bitpay usigned wrapper
    passing a payload will do a POST, otherwise a GET
    """
    headers = {"content-type": "application/json", "X-accept-version": "2.0.0"}
    try:
      if payload:
        response = requests.post(self.uri + path, verify=self.verify, data=json.dumps(payload), headers=headers)
      else:
        response = requests.get(self.uri + path, verify=self.verify, headers=headers)
    except Exception as pro:
      raise BitPayConnectionError('Connection refused')
    return response

  def unsigned_get_request(self, path, payload=None):
    """
    Deprecated, will be removed in 2.4
    """
    return self.unsigned_request('/tokens', payload)
