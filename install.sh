#!/bin/bash

echo "Checking python version"
version=$(python3 -V 2>&1 | cut -d\  -f 2)
version=(${version//./ })

if [[ ${version[0]} -lt 3 ]] || [[ ${version[0]} -eq 3 && ${version[1]} -lt 6 ]]; then
  echo ""
  echo "Need python3.6+ for blake2 && blake2b libs" 1>&2
  exit 1
else
  echo ""
  echo "Python ready to use"
  echo "Now installing 7z package and unpacked"
  sudo apt install p7zip-full
  7z x rockyou.7z
  exit 1
fi
