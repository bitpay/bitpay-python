# BitPay Library for Python
Powerful, flexible, lightweight interface to the BitPay Bitcoin Payment Gateway API.

[![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square)](https://raw.githubusercontent.com/bitpay/bitpay-python/master/LICENSE.txt)
[![Travis](https://img.shields.io/travis/bitpay/bitpay-python.svg?style=flat-square)](https://travis-ci.org/bitpay/bitpay-python)
[![PyPI](https://img.shields.io/pypi/v/bitpay.svg?style=flat-square)](https://pypi.org/project/bitpay)
[![Supported Python versions](https://pypip.in/py_versions/bitpay/badge.svg?style=flat-square)](https://pypi.org/project/bitpay)
[![Scrutinizer](https://img.shields.io/scrutinizer/g/bitpay/bitpay-python.svg?style=flat-square)](https://scrutinizer-ci.com/g/bitpay/bitpay-python/)
[![Coveralls](https://img.shields.io/coveralls/bitpay/bitpay-python.svg?style=flat-square)](https://coveralls.io/r/bitpay/bitpay-python)

This library is only compatible with Python 2.7 and 3.*.

## Getting Started
To get up and running with this library quickly, see these getting started guides:
* https://github.com/bitpay/bitpay-python/blob/master/GUIDE.md
* https://support.bitpay.com/hc/en-us/articles/115003001203-How-do-I-configure-and-use-the-BitPay-Python-Library-
* https://bitpay.com/docs/testing

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

* [GitHub Issues](https://github.com/bitpay/bitpay-python/issues)
  * Open an issue if you are having issues with this library
* [Support](https://help.bitpay.com)
  * BitPay merchant support documentation

Sometimes a download can become corrupted for various reasons.  However, you can verify that the release package you downloaded is correct by checking the md5 checksum "fingerprint" of your download against the md5 checksum value shown on the Releases page.  Even the smallest change in the downloaded release package will cause a different value to be shown!
  * If you are using Windows, you can download a checksum verifier tool and instructions directly from Microsoft here: http://www.microsoft.com/en-us/download/details.aspx?id=11533
  * If you are using Linux or OS X, you already have the software installed on your system.
    * On Linux systems use the md5sum program.  For example:
      * md5sum filename
    * On OS X use the md5 program.  For example:
      * md5 filename
