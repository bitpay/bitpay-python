# chardet's setup.py
import setuptools
setuptools.setup(
    name="bitpay",
    packages=["bitpay"],
    version="2.5.1906.1",
    description="Accept bitcoin with BitPay",
    author="Antonio Buedo",
    author_email="sales-engineering@bitpay.com",
    url="https://github.com/bitpay/bitpay-python",
    download_url="https://github.com/bitpay/bitpay-python/tarball/v2.5.1906",
    keywords=["bitcoin", "payments", "crypto", "cash", "ethereum", "online payments"],
    python_requires=">=2.7.16",
    install_requires=["requests", "ecdsa"],
    classifiers=[
        "Programming Language :: Python :: 2.7",
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        "Development Status :: 5 - Production/Stable",
        'Intended Audience :: Developers',
        'Natural Language :: English',
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Office/Business :: Financial"
    ],
    long_description="""\
        Python Library for integrating with BitPay
        
        This library is a simple way to integrate your application with
        BitPay for taking Bitcoin payments. It exposes three basic 
        functions, authenticating with BitPay, creating invoices, 
        and retrieving invoices. It is not meant as a replacement for 
        the entire BitPay API. However, the key_utils module contains
        all of the tools you need to use the BitPay API for other
        purposes.
        
        This version requires Python 2.7 or later.
        """,
    long_description_content_type='text/markdown'
)
