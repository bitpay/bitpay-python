# BitPay Library for Python 
Powerful, flexible, lightweight interface to the BitPay Bitcoin Payment Gateway API.

[![](https://travis-ci.org/bitpay/bitpay-python.svg?branch=master)](https://travis-ci.org/bitpay/bitpay-python) [![PyPi Package](https://pypip.in/version/bitpay/badge.svg)](https://pypi.python.org/pypi/bitpay/2.2.0)

This library is only compatible with Python 3. Please use the bitpay-python-py2 library for Python 2 installations.

## [Getting Started &raquo;](http://dev.bitpay.com/guides/python.html)

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
