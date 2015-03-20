# BitPay Library for Python 
Powerful, flexible, lightweight interface to the BitPay Bitcoin Payment Gateway API.

[![Supported Python versions](https://pypip.in/py_versions/bitpay/badge.svg)](https://pypi.python.org/pypi/bitpay/)
[![PyPi Package](https://pypip.in/version/bitpay/badge.svg)](https://pypi.python.org/pypi/bitpay/2.2.0)
[![](https://travis-ci.org/bitpay/bitpay-python.svg?branch=master)](https://travis-ci.org/bitpay/bitpay-python)

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

**BitPay Support:**

* [BitPay Labs](https://labs.bitpay.com/c/libraries/python)
  * Post a question in our discussion forums
* [GitHub Issues](https://github.com/bitpay/bitpay-python/issues)
  * Open an issue if you are having issues with this library
* [Support](https://support.bitpay.com)
  * BitPay merchant support documentation

Sometimes a download can become corrupted for various reasons.  However, you can verify that the release package you downloaded is correct by checking the md5 checksum "fingerprint" of your download against the md5 checksum value shown on the Releases page.  Even the smallest change in the downloaded release package will cause a different value to be shown!
  * If you are using Windows, you can download a checksum verifier tool and instructions directly from Microsoft here: http://www.microsoft.com/en-us/download/details.aspx?id=11533
  * If you are using Linux or OS X, you already have the software installed on your system.
    * On Linux systems use the md5sum program.  For example:
      * md5sum filename
    * On OS X use the md5 program.  For example:
      * md5 filename
