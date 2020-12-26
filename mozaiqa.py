#!/usr/bin/env python3
import config
import argparse

from src.archive import RipArchive
from src.foundhash import FoundHash
from src.foundbinary import FoundBinary
from src.identifier import Identifier
from src.passwordinfo import Passwordinfo


def main():
    parser = argparse.ArgumentParser(description=config._list[0],
            add_help=False, usage=config._list[1])
    parser.add_argument("-h", "--help", action="help",
            help="show this help message.")
    parser.add_argument("-m", help="add hash.")
    parser.add_argument("-a", help=config._list[3])
    parser.add_argument("-s", help="checking the capabilities of bruteforce.")
    parser.add_argument("-f", help="add zip archive name.")
    parser.add_argument("-i", help="quick search by hash size.")
    parser.add_argument("-test", action="store_true", help="test the program.")
    args = parser.parse_args()

    try:
        if args.m and args.a:
            finalH = FoundHash(config.__open(), args.a, args.m)
            finalH.md4()
            finalH.md5()
            finalH.shake128_full()
            finalH.shake256_full()
            finalH.sha_full()
            finalH.sha3_full()
            finalH.ripemd160()
            finalH.blake2()
            finalB = FoundBinary(config.__open(), args.a, args.m)
            finalB.base32_64()
        elif args.f:
            finalF = RipArchive(config.__open(), args.f)
            finalF.checkzip()
        elif args.s:
            finalS = Passwordinfo(args.s)
            finalS.finish()
        elif args.i:
            finalI = Identifier(args.i)
            finalI.timetofound()
        elif args.test:
            import time
            import subprocess
            start = time.time()
            subprocess.call("test/test_zip.sh", shell=True)
            time.sleep(5)
            subprocess.call("test/test_hash.sh", shell=True)
            time.sleep(5)
            subprocess.call("test/test_binary.sh", shell=True)
            time.sleep(5)
            print("Completed in {0}".format(time.time()-start))
        else:
            print("Unknown flag.")
    except KeyboardInterrupt:
        print("-"*50)
        print("Program stopped.")
        print("-"*50)

if __name__ == "__main__":
    main()
