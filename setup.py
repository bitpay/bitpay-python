# chardet's setup.py
from distutils.core import setup
setup(
    name = "bitpay",
    packages = ["bitpay"],
    version = "2.4.1905",
    description = "Accept bitcoin with BitPay",
    author = "BitPay Integrations Team",
    author_email = "sales-engineering@bitpay.com",
    url = "https://github.com/bitpay/bitpay-python",
    download_url = "https://github.com/bitpay/bitpay-python/tarball/v2.4.1905",
    keywords = ["bitcoin", "payments", "crypto"],
    install_requires = ["requests", "ecdsa"],
    classifiers = [
"Programming Language :: Python :: 3.7",
"Programming Language :: Python :: 3 :: Only",
"Development Status :: 5 - Production/Stable",
"Environment :: Web Environment",
"Intended Audience :: Developers",
"License :: OSI Approved :: MIT License",
"Operating System :: OS Independent",
"Topic :: Software Development :: Libraries :: Python Modules",
"Topic :: Office/Business :: Financial"
],
    long_description = """\
Python Library for integrating with BitPay
-------------------------------------

This library is a simple way to integrate your application with
BitPay for taking bitcoin payments. It exposes three basic 
functions, authenticating with bitpay, creating invoices, 
and retrieving invoices. It is not meant as a replacement for 
the entire BitPay API. However, the key_utils module contains
all of the tools you need to use the BitPay API for other
purposes.

This version requires Python 3 or later; a Python 2 version is available separately.
"""
)
