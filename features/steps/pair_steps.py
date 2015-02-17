from splinter import Browser
import time
import os
import six
from bitpay.client import Client

ROOT_ADDRESS = os.environ['RCROOTADDRESS']
USER_NAME = os.environ['RCTESTUSER']
PASSWORD = os.environ['RCTESTPASSWORD']
PEM = '-----BEGIN EC PRIVATE KEY-----\nMHQCAQEEICg7E4NN53YkaWuAwpoqjfAofjzKI7Jq1f532dX+0O6QoAcGBSuBBAAK\noUQDQgAEjZcNa6Kdz6GQwXcUD9iJ+t1tJZCx7hpqBuJV2/IrQBfue8jh8H7Q/4vX\nfAArmNMaGotTpjdnymWlMfszzXJhlw==\n-----END EC PRIVATE KEY-----\n'
client = Client()
exception = None

@given(u'the user pairs with BitPay with a valid pairing code')
def step_impl(context):
  claim_code = get_claim_code_from_server()
  global client
  client = Client(api_uri=ROOT_ADDRESS, insecure=True, pem=PEM)
  client.pair_pos_client(claim_code)
  assert client.tokens['pos']

@then(u'the user is paired with BitPay')
def step_impl(context):
  assert client.verify_tokens()

@given(u'the user fails to pair with a semantically {valid} code {code}')
def step_impl(context, code, valid):
  time.sleep(0.5)
  try: 
    client.pair_pos_client(code)
  except Exception as error:
    global exception
    exception = error

@when(u'the user fails to pair with BitPay because of an incorrect port')
def step_impl(context):
  time.sleep(0.5)
  badAddress = ROOT_ADDRESS.split(":")
  badAddress = badAddress[0] + ":" + badAddress[1] + ":999"
  newclient = Client(api_uri=badAddress, insecure=True, pem=PEM)
  try:
    newclient.pair_pos_client("1a2C3d4")
    raise "That should totally not have worked"
  except Exception as error:
    global exception
    exception = error

@then(u'they will receive a {error} matching {message}')
def step_impl(context, error, message):
  assert exception.__class__.__name__ == error and exception.args[0] == message

def get_claim_code_from_server():
  browser = Browser('phantomjs', service_args=['--ignore-ssl-errors=true'])
  browser.visit(ROOT_ADDRESS + "/merchant-login")
  browser.fill_form({"email": USER_NAME, "password": PASSWORD})
  browser.find_by_id("loginButton")[0].click()
  time.sleep(1)
  browser.visit(ROOT_ADDRESS + "/api-tokens")
  browser.find_by_css(".token-access-new-button").find_by_css(".btn").find_by_css(".icon-plus")[0].click()
  browser.find_by_id("token-new-form").find_by_css(".btn")[0].click()
  return browser.find_by_css(".token-claimcode")[0].html
  

