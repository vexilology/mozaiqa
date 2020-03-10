#!/usr/bin/env python3
import argparse
import config
from src.algorithms import FoundHash, FoundBinary
from src.passwordinfo import Passwordinfo

def main():
    try:
        myfile = open("rockyou.txt", "r", encoding="utf-8", errors="ignore")
    except FileNotFoundError:
        print(config.red, "-" * 50)
        print("Error: txt file not found, check folder.")
        print("-" * 50)
        quit()

    parser = argparse.ArgumentParser(description="[*]Mozaiqa script")
    parser.add_argument("-m", type=str, help="Add Hash.")
    parser.add_argument("-a", type=str, help="md2, md4, md5,\
            sha1, sha224, sha256, sha384, sha512, ripemd160,\
            blake2s-256, blake2b-512")
    parser.add_argument("-s", type=str, help="Checking the capabilities of bruteforce.")
    args = parser.parse_args()

    try:
        finalH = FoundHash(myfile, args.a, args.m)
        finalB = FoundBinary(myfile, args.a, args.m)
        finalS = Passwordinfo(args.s)

        finalH.md4()
        finalH.md5()
        finalH.sha_full()
        finalH.ripemd160()
        finalH.blake2()
        finalB.base32_64()
        finalB.ascii85()
        finalS.finish()
    except KeyboardInterrupt:
        print(config.green, "-" * 50)
        print("Program stopped with Ctrl+C.")
        print("-" * 50)
        quit()

if __name__ == "__main__":
    main()
