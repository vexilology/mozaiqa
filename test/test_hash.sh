#!/bin/bash

test_md5=67881381dbc68d4761230131ae0008f7
test_ripemd160=bbb5d2039830c21b26cfd525467da9f7229a7d38
test_sha1=b03b74363bbb6ee42ce248c7a5344e92ffe76cc7
test_sha3_256=f396c5df2b7c3db9a2b8cc44f2736be8bd113cdb5ab9e99c5cd8eb2d3fb9bbb0
test_blake2s=b18d98e183afee28b34c39944bcb5e643f8ce1e64b35c4c9536c027297c2fbbf
test_blake2b=53b847b397ceb85a1d11c54214dd324007f3c19a29bb50c1e34754aa54370c3fcecfb3dbb357a06f0272864c55523e44afc2ca2ae4d40d05e452f4748223a8f9
test_sha3_512=8f1a173c87f78b8d69f5406b3b9bf1593b459b3133aa9a326894ebc99cc18e7c177578db8b13fbec5dff76cb38d9410614121a51a2aeaa618f57efd7a8fb0778
test_sha512=da34e82ebc71ccc880c639cfbdaf94b3a01c2b98c4e54d9e0ef3256a17b01db280fc8623b6de2a44dea0a5d534f73919434944f623bc037e331675567c6f05ee

./mozaiqa.py -m $test_md5 -a md5
echo ""
echo "MD5 :: TEST PASSED..."
echo ""

./mozaiqa.py -m $test_ripemd160 -a ripemd160
echo ""
echo "RIPEMD160 :: TEST PASSED..."
echo ""

./mozaiqa.py -m $test_sha1 -a sha1
echo ""
echo "SHA1 :: TEST PASSED..."
echo ""

./mozaiqa.py -m $test_sha3_256 -a sha3-256
echo ""
echo "SHA3-256 :: TEST PASSED..."
echo ""

./mozaiqa.py -m $test_blake2s -a blake2s-256
echo ""
echo "BLAKE2S-256 :: TEST PASSED..."
echo ""

./mozaiqa.py -m $test_blake2b -a blake2b-512
echo ""
echo "BLAKE2B-512 :: TEST PASSED..."
echo ""

./mozaiqa.py -m $test_sha3_512 -a sha3-512
echo ""
echo "SHA3-512 :: TEST PASSED..."
echo ""

./mozaiqa.py -m $test_sha512 -a sha512
echo ""
echo "SHA512 :: TEST PASSED..."
echo "Exit, waiting 5s"
