#!/bin/bash

touch abs.txt
echo "123-123-123-876-098" > abs.txt
zip -P fuckyou1 hackme.zip abs.txt
rm abs.txt
./mozaiqa.py -f hackme.zip
rm hackme.zip
rm abs.txt
echo ""
echo "ZIP :: TEST PASSED..."
echo "Waiting 10s"
echo ""
