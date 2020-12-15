#!/bin/bash

./mozaiqa.py -m 67881381dbc68d4761230131ae0008f7 -a md5
echo ""
echo "MD5 :: TEST PASSED..."
echo ""

./mozaiqa.py -m b03b74363bbb6ee42ce248c7a5344e92ffe76cc7 -a sha1
echo ""
echo "SHA1 :: TEST PASSED..."
echo ""

./mozaiqa.py -m da34e82ebc71ccc880c639cfbdaf94b3a01c2b98c4e54d9e0ef3256a17b01db280fc8623b6de2a44dea0a5d534f73919434944f623bc037e331675567c6f05ee -a sha512
echo ""
echo "SHA512 :: TEST PASSED..."
echo "Exit, waiting 10s"
