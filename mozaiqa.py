#!/usr/bin/env python3
import config
import argparse
from src.archive import RipArchive
from src.passwordinfo import Passwordinfo
from src.algorithms import FoundHash, FoundBinary

def main():
    try:
        myfile = open("rockyou.txt", "r",
                encoding="utf-8", errors="ignore")
    except FileNotFoundError:
        print(config.red, "-" * 50)
        print("Error: txt file not found, check folder.")
        print("-" * 50)
        quit()

    parser = argparse.ArgumentParser(description="name: mozaiqa script",
            add_help=False, usage="./mozaiqa.py [-m] [-a] [-s] [-f]")
    parser.add_argument("-h", "--help", action="help",
            help="show this help message.")
    parser.add_argument("-m", help="add hash.")
    parser.add_argument("-a", help="md2, md4, md5,\
            sha1, sha224, sha256, sha384, sha512, ripemd160,\
            blake2s-256, blake2b-512")
    parser.add_argument("-s", help="checking the \
            capabilities of bruteforce.")
    parser.add_argument("-f", help="add zip archive name.")
    args = parser.parse_args()
    if args is False:
        SystemExit

    try:
        if args.m and args.a:
            finalH = FoundHash(myfile, args.a, args.m)
            finalB = FoundBinary(myfile, args.a, args.m)
            finalH.md4()
            finalH.md5()
            finalH.sha_full()
            finalH.ripemd160()
            finalH.blake2()
            finalB.base32_64()
            finalB.ascii85()
        elif args.f:
            finalF = RipArchive(myfile, args.f)
            finalF.checkzip()
        elif args.s:
            finalS = Passwordinfo(args.s)
            finalS.finish()
    except KeyboardInterrupt:
        print(config.green, "-" * 50)
        print("Program stopped with Ctrl+C.")
        print("-" * 50)

if __name__ == "__main__":
    main()
