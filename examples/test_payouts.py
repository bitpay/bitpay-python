from bitpay.exceptions import *
import bitpay.key_utils as bku
from bitpay.client import *
import pprint
import requests
import json
import os.path
import sys

#API_HOST = "https://bitpay.com" #for production, live bitcoin
API_HOST = "https://test.bitpay.com" #for testing, testnet bitcoin
KEY_FILE = "tmp/key.priv"
TOKEN_FILE = "tmp/token.priv"
pp = pprint.PrettyPrinter(indent=4)

# check if there is a preexisting key file
if os.path.isfile(KEY_FILE):
    f = open(KEY_FILE, 'r')
    key = f.read()
    f.close()
    print("Creating a bitpay client using existing private key from disk.")
else:
    key = bku.generate_pem()
    f = open(KEY_FILE, 'w')
    f.write(key)
    f.close()

client = Client(API_HOST, False, key)

def fetch_token(facade):
    if os.path.isfile(TOKEN_FILE + facade):
        f = open(TOKEN_FILE + facade, 'r')
        token = f.read()
        f.close()
        print("Reading " + facade + " token from disk.")
        client.tokens[facade] = token
    else:
        pairingCode = client.create_token(facade)
        print("Creating " + facade + " token.")
        print("Please go to:  %s/dashboard/merchant/api-tokens  then enter \"%s\" then click the \"Find\" button, then click \"Approve\"" % (API_HOST, pairingCode))
        if int(sys.version[0]) == 3:
            input("When you've complete the above, hit enter to continue...")
        else:
            raw_input("When you've complete the above, hit enter to continue...")
        print("token is: %s" % client.tokens[facade])
        f = open(TOKEN_FILE + facade, 'w')
        f.write(client.tokens[facade])
        f.close()

def get_from_bitpay_api(client, uri, token):
    payload = "?token=%s" % token
    xidentity = bku.get_compressed_public_key_from_pem(client.pem)
    xsignature = bku.sign(uri + payload, client.pem)
    headers = {"content-type": "application/json",
                "X-Identity": xidentity,
                "X-Signature": xsignature, "X-accept-version": "2.0.0"}
    try:
        pp.pprint(headers)
        print(uri + payload)
        response = requests.get(uri + payload, headers=headers, verify=client.verify)
    except Exception as pro:
        raise BitPayConnectionError(pro.args)
    if response.ok:
        return response.json()['data']
    client.response_error(response)

"""
POST to any resource
Make sure to include the proper token in the params
"""
def post_to_bitpay_api(client, uri, resource, params):
    payload = json.dumps(params)
    uri = uri + "/" + resource
    xidentity = key_utils.get_compressed_public_key_from_pem(client.pem)
    xsignature = key_utils.sign(uri + payload, client.pem)
    headers = {"content-type": "application/json",
               "X-Identity": xidentity,"X-Signature": xsignature,
               "X-accept-version": "2.0.0"}
    try:
        response = requests.post(uri, data=payload, headers=headers,
                                 verify=client.verify)
    except Exception as pro:
        raise BitPayConnectionError(pro.args)
    if response.ok:
        return response.json()['data']
    client.response_error(response)

fetch_token("payroll")

#create a payroll token
token = client.tokens['payroll']
print("Creating a payout batch now")
print("token = " + token)
# posting a payout batch
params = {"token":token, "notificationURL":"https://hookb.in/3OBkOPk23ouKeKj2M2WQ", "effectiveDate":"2019-05-21", "amount":"10","currency":"USD","instructions":[ {"label":"Test1","address":"mx2Wv5j8SrPnxAQtNB3uf8mii1Vc5UDKsZ","amount":"7"},{"label":"Test2","address":"mx2Wv5j8SrPnxAQtNB3uf8mii1Vc5UDKsZ","amount":"3"}]}
payoutBatch = post_to_bitpay_api(client, "https://test.bitpay.com", "payouts", params)
pp.pprint(payoutBatch)

