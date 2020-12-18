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

test_base32=`readJson hash_examples.json base32` || exit 1;
./mozaiqa.py -m $test_base32 -a base32
echo ""
echo "BASE32 :: TEST PASSED..."
echo ""

test_base64=`readJson hash_examples.json base64` || exit 1;
./mozaiqa.py -m $test_base64 -a base64
echo ""
echo "BASE64 :: TEST PASSED..."
echo ""

test_ascii85=`readJson hash_examples.json ascii85` || exit 1;
./mozaiqa.py -m $test_ascii85 -a ascii85
echo ""
echo "ASCII85 :: TEST PASSED..."
echo "Exit, waiting 5s"
