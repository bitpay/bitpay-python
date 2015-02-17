from bitpay.exceptions import *
from bitpay import key_utils
import requests
import json
import re

class Client:
  def __init__(self, api_uri="https://bitpay.com", insecure=False, pem=key_utils.generate_pem()):
    self.uri = api_uri
    self.verify = not(insecure)
    self.pem = pem
    self.client_id = key_utils.get_sin_from_pem(pem)
    self.tokens = None
    self.user_agent = 'bitpay-python'

  def pair_pos_client(self, code):
    if re.match("^\w{7,7}$", code) is None:
      raise BitPayArgumentError("pairing code is not legal")
    payload = {'id': self.client_id, 'pairingCode': code}
    headers = {"content-type": "application/json", "accept": "application/json", "X-accept-version": "2.0.0"}
    try:
      response = requests.post(self.uri + "/tokens", verify=self.verify, data=json.dumps(payload), headers=headers)
    except Exception as pro:
      raise BitPayConnectionError('Connection refused')
    if response.ok:
      self.tokens = self.token_from_response(response.json())
      return True
    raise BitPayBitPayError('%(code)d: %(message)s' % {'code': response.status_code, 'message': response.json()['error']})

  def token_from_response(self, responseJson):
    token = responseJson['data'][0]['token']
    facade = responseJson['data'][0]['facade']
    return {facade: token}

  def verify_tokens(self):
    xidentity = key_utils.get_compressed_public_key_from_pem(self.pem)
    url = self.uri + "/tokens"
    print(url)
    xsignature = key_utils.sign(self.uri + "/tokens", self.pem)
    print(xsignature)
    headers = {"content-type": "application/json", 'accept': 'application/json', 'X-Identity': xidentity, 'X-Signature': xsignature, 'X-accept-version': '2.0.0'}
    response = requests.get(self.uri + "/tokens", headers=headers, verify=self.verify)
    if response.ok:
      allTokens = response.json()['data']
      selfKeys = self.tokens.keys() 
      matchedTokens = [token for token in allTokens for key in selfKeys if token.get(key) == self.tokens.get(key)]
      if not matchedTokens:
        return False
      return True
    raise BitPayBitPayError('%(code)d: %(message)s' % {'code': response.status_code, 'message': response.json()['error']})
