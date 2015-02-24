# BitPay Library for Python [![](https://travis-ci.org/bitpay/bitpay-python.svg?branch=master)](https://travis-ci.org/bitpay/bitpay-python) [![PyPi Package](https://pypip.in/version/bitpay/badge.svg)](https://pypip.in/version/bitpay)
Powerful, flexible, lightweight interface to the BitPay Bitcoin Payment Gateway API.

## Installation

BitPay's python library was developed in Python 3.4.2. The recommended method of installion is using pip.

`pip install 'bitpay'`

## Basic Usage

The bitpay library allows authenticating with BitPay, creating invoices, and retrieving invoices.
  
### Pairing with Bitpay.com

Before pairing with BitPay.com, you'll need to log in to your BitPay account and navigate to /api-tokens. Generate a new pairing code and use it in the next step. You can try out various functions using the Python REPL. In this example, it's assumed that we are working against the bitpay test server and have generated the pairing code "abcdefg".

    > from bitpay.client import Client
    > client = Client(api_uri="https://test.bitpay.com") #if api_uri is not passed, it defaults to "https://bitpay.com"
    > client.pair_pos_client("abcdefg")

### To create an invoice with a paired client:

Using the same web client from the last step:

    > client.create_invoice({"price": 20, "currency": "USD", "token": client.tokens['pos']})

That will return the invoice as JSON. Other parameters can be sent, see the [BitPay REST API documentation](https://bitpay.com/api#resource-Invoices) for details.

## API Documentation

API Documentation is available on the [BitPay site](https://bitpay.com/api).

## Running the Tests

Before running the behavior tests, you will need a test.bitpay.com account and you will need to set the local constants. 

To set constants:
    > source tasks/set_constants.sh "https://test.bitpay.com" your@email yourpassword

To run unit tests:
    > nosetests

To run behavior tests:
    > behave
    
## Found a bug?
Let us know! Send a pull request or a patch. Questions? Ask! We're here to help. We will respond to all filed issues.
