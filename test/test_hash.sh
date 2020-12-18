#!/bin/bash

function readJson {
  UNAMESTR=`uname`
  if [[ "$UNAMESTR" == 'Linux' ]]; then
    SED_EXTENDED='-r'
  elif [[ "$UNAMESTR" == 'Darwin' ]]; then
    SED_EXTENDED='-E'
  fi;

  VALUE=`grep -m 1 "\"${2}\"" ${1} | sed ${SED_EXTENDED} 's/^ *//;s/.*: *"//;s/",?//'`

  if [ ! "$VALUE" ]; then
    echo "Error: Cannot find \"${2}\" in ${1}" >&2;
    exit 1;
  else
    echo $VALUE;
  fi;
}

test_md5=`readJson hash_examples.json md5` || exit 1;
./mozaiqa.py -m $test_md5 -a md5
echo ""
echo "MD5 :: TEST PASSED..."
echo ""

test_ripemd160=`readJson hash_examples.json ripemd160` || exit 1;
./mozaiqa.py -m $test_ripemd160 -a ripemd160
echo ""
echo "RIPEMD160 :: TEST PASSED..."
echo ""

test_sha1=`readJson hash_examples.json sha1` || exit 1;
./mozaiqa.py -m $test_sha1 -a sha1
echo ""
echo "SHA1 :: TEST PASSED..."
echo ""

test_sha3_256=`readJson hash_examples.json sha3_256` || exit 1;
./mozaiqa.py -m $test_sha3_256 -a sha3-256
echo ""
echo "SHA3-256 :: TEST PASSED..."
echo ""

test_shake128_256=`readJson hash_examples.json shake128_256` || exit 1;
./mozaiqa.py -m $test_shake128_256 -a shake128-256
echo ""
echo "SHAKE128-256 :: TEST PASSED..."
echo ""

test_shake256_256=`readJson hash_examples.json shake256_256` || exit 1;
./mozaiqa.py -m $test_shake256_256 -a shake256-256
echo ""
echo "SHAKE256-256 :: TEST PASSED..."
echo ""

test_blake2s=`readJson hash_examples.json blake2s` || exit 1;
./mozaiqa.py -m $test_blake2s -a blake2s-256
echo ""
echo "BLAKE2S-256 :: TEST PASSED..."
echo ""

test_blake2b=`readJson hash_examples.json blake2b` || exit 1;
./mozaiqa.py -m $test_blake2b -a blake2b-512
echo ""
echo "BLAKE2B-512 :: TEST PASSED..."
echo ""

test_sha3_512=`readJson hash_examples.json sha3_512` || exit 1;
./mozaiqa.py -m $test_sha3_512 -a sha3-512
echo ""
echo "SHA3-512 :: TEST PASSED..."
echo ""

test_shake128_512=`readJson hash_examples.json shake128_512` || exit 1;
./mozaiqa.py -m $test_shake128_512 -a shake128-512
echo ""
echo "SHAKE128-512 :: TEST PASSED..."
echo ""

test_shake256_512=`readJson hash_examples.json shake256_512` || exit 1;
./mozaiqa.py -m $test_shake256_512 -a shake256-512
echo ""
echo "SHAKE256-512 :: TEST PASSED..."
echo ""

test_sha512=`readJson hash_examples.json sha512` || exit 1;
./mozaiqa.py -m $test_sha512 -a sha512
echo ""
echo "SHA512 :: TEST PASSED..."
echo "Waiting 5s"
echo ""
