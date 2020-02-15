#!/usr/bin/env python3
import argparse
from src.algorithms import FoundHash, FoundBinary
from src.passwordinfo import Passwordinfo

def main():
    try:
        myfile = open("rockyou.txt", "r", encoding="utf-8", errors="ignore")
    except:
        print("\033[31m-" * 50)
        print("Error: txt file not found, check folder.")
        print("-" * 50)
        quit()

    parser = argparse.ArgumentParser()
    parser.add_argument("-m", type=str, help="hash")
    parser.add_argument("-a", type=str, help="algorithm")
    parser.add_argument("-s", type=str, help="passwordinfo")
    args = parser.parse_args()

    finalH = FoundHash(myfile, args.a, args.m)
    finalB = FoundBinary(myfile, args.a, args.m)
    finalS = Passwordinfo(args.s)

    finalH.md2()
    finalH.md4()
    finalH.md5()
    finalH.sha_full()
    finalH.ripemd160()
    finalH.sha3_full()
    finalH.keccak_full()
    finalH.shake_full()
    finalB.base32_64()
    finalB.ascii85()
    finalS.finish()

if __name__ == "__main__":
    main()
