#!/bin/bash

touch abs.txt
echo "123-123-123-876-098" > abs.txt
zip -P fuckyou1 hackme.zip abs.txt
rm abs.txt
if ./mozaiqa.py -f hackme.zip; then
  echo "about abs.txt"
  cat abs.txt
  rm hackme.zip
  rm abs.txt
  echo ""
  echo "ZIP :: TEST PASSED..."
  echo "Waiting 5s"
  echo ""
else
  echo ""
  echo "ZIP :: TEST FAILED..."
  echo "Waiting 5s"
  echo ""
fi
