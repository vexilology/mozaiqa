#!/usr/bin/env python3
import config
import argparse

from src.archive import RipArchive
from src.foundhash import FoundHash
from src.identifier import Identifier
from src.foundbinary import FoundBinary
from src.passwordinfo import Passwordinfo

def main():
    try:
        myfile = open("rockyou.txt", "r",
                encoding="utf-8", errors="ignore")
    except FileNotFoundError:
        print(config.red, "-" * 50)
        print("Error: txt file not found, check folder.")
        print("-" * 50)
        exit(1)

    parser = argparse.ArgumentParser(description="*** mozaiqa script ***",
            add_help=False, usage="./mozaiqa.py [-m] [-a] [-s] [-f]")
    parser.add_argument("-h", "--help", action="help",
            help="show this help message.")
    parser.add_argument("-m", help="add hash.")
    parser.add_argument("-a", help="md2, md4, md5,\
            sha1, sha224, sha256, sha384, sha512, ripemd160,\
            blake2s-256, blake2b-512, \
            base32, base64, ascii85.")
    parser.add_argument("-s", help="checking the \
            capabilities of bruteforce.")
    parser.add_argument("-f", help="add zip archive name.")
    parser.add_argument("-i", help="quick search by hash size.")
    args = parser.parse_args()
    if args is False:
        SystemExit

    try:
        if args.m and args.a:
            finalH = FoundHash(myfile, args.a, args.m)
            finalH.md4()
            finalH.md5()
            finalH.sha_full()
            finalH.ripemd160()
            finalH.blake2()
            finalB = FoundBinary(myfile, args.a, args.m)
            finalB.base32_64()
        elif args.f:
            finalF = RipArchive(myfile, args.f)
            finalF.checkzip()
        elif args.s:
            finalS = Passwordinfo(args.s)
            finalS.finish()
        elif args.i:
            finalI = Identifier(args.i)
            finalI.timetofound()
        else:
            print("Use flags. For more info ./mozaiqa.py -h")
    except KeyboardInterrupt:
        print(config.green, "-" * 50)
        print("Program stopped with Ctrl+C.")
        print("-" * 50)

if __name__ == "__main__":
    main()
